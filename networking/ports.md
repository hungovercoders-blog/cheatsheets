
# Ports

Ports are separate channels for same protocol. For example, HTTP and HTTPS are both HTTP protocols, but they are on different ports. Ports are used to separate different services on the same server. For example, a server can have a web server, a mail server, and a file server all running on the same machine. Each of these services will be listening on a different port. When a client wants to connect to one of these services, it will specify the port number in the connection request. The server will then know which service the client wants to connect to.

## Live Ports

- 80: HTTP
- 443: HTTPS
- 22: SSH

## Development Ports

Ports 8080, 8000, 3000, and 3001 are commonly used for web development and other applications for several reasons:

Non-privileged Ports:

Ports below 1024 are "well-known ports" and on UNIX-like systems, binding to one of these ports requires root privileges. To avoid having to run applications as root, developers often choose ports above 1024 for their applications.
Default Configuration:

Many development tools and applications use these ports by default. For instance:
- 8080: Common alternative for HTTP (which is on port 80). Tools like Tomcat and Jetty use this port by default.
- 8000: Another common alternative for HTTP. For instance, Django's development server starts on this port by default.
- 3000: Default for tools like React's development server (create-react-app) and Rails (in some configurations).
- 3001: Sometimes used as a secondary port. If you start another instance of a tool that defaults to 3000, it might automatically pick 3001.
Convention:

Over time, as these ports have been adopted by popular tools, they have become somewhat of a convention in the developer community. When developers see one of these ports, they often have a good guess at what might be running.
Avoiding Conflicts:

It's important to remember that two applications can't bind to the same port on the same interface at the same time. By convention, certain applications default to these ports to reduce the chance of conflicts.
Easy to Remember:

These ports are easy to remember, which can be beneficial during development.
It's worth noting that while these ports are commonly used in development environments, in a production setting, applications will typically be behind a reverse proxy (like Nginx or Apache) that listens on the standard ports (like 80 for HTTP and 443 for HTTPS) and forwards requests to the application on these higher-numbered ports.