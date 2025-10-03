from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
# Importamos SOLO las funciones de la lógica de negocio
from post import ( # <-- CAMBIADO de .post a post
    get_all_posts,
    get_post_by_id,
    create_post,
    update_post,
    delete_post
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eduardogodoymedina'

# Rutas estáticas ---------------------------------

@app.route("/", methods=["GET"])
def index():
    name_page = "blog"
    return render_template("index.html", name_page=name_page)

@app.route("/about", methods=["GET"])
def about():
    name_page = "about"
    return render_template("about.html", name_page=name_page)

# Rutas de Posts (CRUD) ---------------------------

@app.route("/posts", methods=["GET"])
def posts_list():
    posts = get_all_posts()
    
    # Soporte JSON (Requisito Opcional)
    if request.args.get('format') == 'json':
        # jsonify convierte la lista de objetos Row de SQLite (que actúan como dicts) a JSON
        return jsonify(posts) 

    return render_template("post/post_list.html", posts_list=posts)

@app.route('/posts/<int:post_id>', methods=['GET'])
def posts_detail(post_id):
    post = get_post_by_id(post_id)
    
    if post is None:
        # Devolver 404 si el post no existe
        if request.args.get('format') == 'json':
             return jsonify({'error': 'Post no encontrado'}), 404
        flash('Post no encontrado.', 'error')
        return redirect(url_for('posts_list'))

    # Soporte JSON (Requisito Opcional)
    if request.args.get('format') == 'json':
        # Convertimos la única fila a JSON. dict() asegura que sea un diccionario estándar.
        return jsonify(dict(post)) 

    return render_template('post/post.html', post=post)

@app.route("/posts/create", methods=["GET", "POST"])
def posts_create():
    if request.method == "GET":
        return render_template("post/create.html")
    
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        
        # Validación de datos (Requisito 2)
        if not title:
            flash('El título es requerido.', 'error')
        elif not content:
            flash('El contenido es requerido.', 'error')
        else:
            # Si la validación es exitosa
            create_post(title, content)
            flash(f'Post "{title}" creado exitosamente.', 'success') # Mensaje de éxito
            return redirect(url_for('posts_list'))

        # Si hay un error, vuelve al formulario, manteniendo los datos ingresados
        return render_template("post/create.html", title=title, content=content)

@app.route('/posts/edit/<int:post_id>', methods=['GET', 'POST'])
def posts_edit(post_id):
    post = get_post_by_id(post_id)
    if post is None:
        flash('Post no encontrado.', 'error')
        return redirect(url_for('posts_list'))

    if request.method == "GET":
        return render_template('post/update.html', post=post)
        
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        # Validación de datos
        if not title:
            flash('El título es requerido.', 'error')
        elif not content:
            flash('El contenido es requerido.', 'error')
        else:
            # Si la validación es exitosa
            update_post(post_id, title, content)
            flash(f'Post "{title}" actualizado exitosamente.', 'success') # Mensaje de éxito
            return redirect(url_for('posts_list'))
            
        # Si hay un error, vuelve al formulario, pero usamos 'post'
        # que ya contiene el ID del post para la acción del formulario.
        # También pasamos los datos del formulario (title, content) para pre-llenar.
        return render_template('post/update.html', post=post, title=title, content=content)

@app.route('/posts/delete/<int:post_id>', methods=['DELETE'])
def posts_delete(post_id):
    # Llama a la función importada para borrar
    delete_post(post_id)
    return ""

#if __name__ == '__main__':
    # Nota: Si el entorno virtual está configurado como paquete,
    # es posible que debas cambiar el inicio o usar 'flask run'.
#   app.run(debug=True)
# Usar 'flask run' en la terminal para correr la app