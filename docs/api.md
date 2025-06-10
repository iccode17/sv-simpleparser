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
      Param(ptype='integer', name='DATA_WIDTH', dim=None, dim_unpacked='', comment=())
      Param(ptype='integer', name='TEST', dim=None, dim_unpacked='', comment=())
      Port(direction='input', ptype='unsigned', name='A', dim='[DATA_WIDTH-1:0]', dim_unpacked='', comment=('This is a test', 'This is another test'))
      Port(direction='input', ptype='unsigned', name='B', dim='[DATA_WIDTH-1:0]', dim_unpacked='', comment=())
      Port(direction='output', ptype='unsigned', name='X', dim='[DATA_WIDTH:0]', dim_unpacked='', comment=())
      ModuleInstance(name='u_test_module', module='test_module')

    ```

See [Datamodel](./api-datamodel.md) for a full reference.
