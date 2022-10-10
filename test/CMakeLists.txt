configure_lit_site_cfg(${CMAKE_CURRENT_SOURCE_DIR}/lit.site.cfg.py.in
                       ${CMAKE_CURRENT_BINARY_DIR}/lit.site.cfg.py)
configure_lit_site_cfg(${CMAKE_CURRENT_SOURCE_DIR}/Unit/lit.site.cfg.py.in
                       ${CMAKE_CURRENT_BINARY_DIR}/Unit/lit.site.cfg.py)

add_custom_target(lwvm-test-depends
                  DEPENDS LWVMUnitTests
                          FileCheck
                          not)

set(LWVM_LIT_PARAMS lwvm_site_config=${CMAKE_CURRENT_BINARY_DIR}/lit.site.cfg.py
                    lwvm_unit_site_config=${CMAKE_CURRENT_BINARY_DIR}/Unit/lit.site.cfg.py)
     
add_lit_testsuite(check-lwvm "Running LWVM lit test suite"
  ${CMAKE_CURRENT_BINARY_DIR}
  PARAMS ${LWVM_LIT_PARAMS}
  DEPENDS lwvm-test-depends)

add_lit_testsuites(LWVM ${CMAKE_CURRENT_SOURCE_DIR}
                   PARAMS ${LWVM_LIT_PARAMS}
                   DEPENDS lwvm-test-depends)
