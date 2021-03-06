from distutils.core import setup, Extension

x25x_hash_module = Extension('x25x_hash',
                               sources = ['x25x_module.c',
                                          'x25x.c',
                                          'sph/extra.c',
                                          'sph/lane.c',
                                          'sph/panama.c',
                                          'sph/blake.c',
                                          'sph/blake2s.c',
                                          'sph/echo.c', 
                                          'sph/groestl.c',  
                                          'sph/haval.c',    
                                          'sph/keccak.c',  
                                          'sph/shavite.c',  
                                          'sph/SWIFFTX.c',
                                          'sph/bmw.c',  
                                          'sph/fugue.c',
                                          'sph/hamsi.c',    
                                          'sph/luffa.c',   
                                          'sph/simd.c',
                                          'sph/sha2.c',
                                          'sph/sph_sha2.c',
                                          'sph/sph_sha2big.c',
                                          'sph/whirlpool.c',
                                          'sph/cubehash.c',  
                                          'sph/gost_streebog.c',  
                                          'sph/jh.c',  
                                          'sph/sponge.c',
                                          'sph/lyra2.c',   
                                          'sph/shabal.c',  
                                          'sph/skein.c', 
                                          'sph/tiger.c'],
                            include_dirs=['.', './sph'])

setup (name = 'x25x_hash',
       version = '1.0',
       ext_modules = [x25x_hash_module])
