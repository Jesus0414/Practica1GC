from OpenGL.GL import *
from glew_wish import *
import glfw 
import random
import time

def main():
    #Incia glfw
    if not glfw.init():
        return
    
    #Crea la ventana, independientemente del SO que usemos
    window = glfw.create_window(800, 800, "Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4) #CUANDO NECESITA REALIZAR AJUSTE PARA NO TENER PERDIDAS
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3) #LA VERSION A TRABAJAR
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3) #LA VERSION A TRABAJAR
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE) #COMPATIBILIDAD CON VERSIONES PASADA
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE) #CONFIGURACION DE DEFAULT

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Estabblecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemosversiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)
    
    #second = time.second
    #print(second)

    while not glfw.window_should_close(window):
        #Establece region de dibujo
        glViewport(0,0,800,600)
        #Establece el color de borrado
        red = random.random() 
        green = random.random()
        blue = random.random() 

        glClearColor(red,green,blue,1)
        #Borra El contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar

        #preuntar si hubo entradas de perdifericos(mouse, teclado, control, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()
