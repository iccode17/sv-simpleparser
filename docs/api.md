# Application Programming Interface (API)

::: sv_simpleparser
    options:
        members: []


!!! example "Usage is simple"

    ```python
    >>> import sv_simpleparser

    >>> file = sv_simpleparser.parse_file("examples/adder.sv")
    >>> for module in file.modules:
    ...     print(repr(module.name))
    ...     for param in module.params:
    ...         print(" ", repr(param))
    ...     for port in module.ports:
    ...         print(" ", repr(port))
    ...     for inst in module.insts:
    ...         print(" ", repr(inst))
    'adder'
      Param(ptype='integer', name='DATA_WIDTH', dim='', dim_unpacked='', ifdefs=(), comment=())
      Param(ptype='integer', name='TEST', dim='', dim_unpacked='', ifdefs=(), comment=())
      Port(direction='input', ptype='', dtype='unsigned', name='A', dim='[DATA_WIDTH-1:0]', dim_unpacked='', ifdefs=(), comment=('This is a test', 'This is another test'))
      Port(direction='input', ptype='', dtype='unsigned', name='B', dim='[DATA_WIDTH-1:0]', dim_unpacked='', ifdefs=(), comment=())
      Port(direction='output', ptype='', dtype='unsigned', name='X', dim='[DATA_WIDTH:0]', dim_unpacked='', ifdefs=(), comment=())
      ModuleInstance(name='u_test_module', module='test_module')


    ```

See [Datamodel](./api-datamodel.md) for a full reference.
