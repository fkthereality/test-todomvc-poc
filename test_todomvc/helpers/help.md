require.s.contexts contains private data regarding all contexts that RequireJS knows about. The default context if you do not use the context configuration option is called _ so require.s.contexts._ contains private data regarding the default context.

The registry field of the context data contains a map that hold module information temporarily. A module will be in that map after it has been requested but only until it has been loaded.

The defined field contains a map of all modules defined in
the context. You could conceivably access it directly but there's no clear reason to do this since require.defined(id) will tell you whether the module named by id is defined in the context to which require belongs. (Different contexts get different instances of require so a require function knows which context it originated from.)

"Object.keys(require.s.contexts._.defined).length == 39"