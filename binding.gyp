{
  'targets': [
    {
      'target_name': 'bcrypt_lib',
      'sources': [
        'src/blowfish.cc',
        'src/bcrypt.cc',
        'src/bcrypt_node.cc'
      ],
      'conditions': [
        [ 'OS=="win"', {
          
          # tepez: this solves 
          # fatal error LNK1181: cannot open input file 'kernel32.lib'
    		  'msvs_settings': {
  			    'VCLinkerTool': {
				      'AdditionalLibraryDirectories': 'c:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Lib\\x64'
			      }
	        },
          
          
          'conditions': [
            # "openssl_root" is the directory on Windows of the OpenSSL files
            ['target_arch=="x64"', {
              'variables': {
                'openssl_root%': 'C:/OpenSSL-Win64'
              },
            }, {
              'variables': {
                'openssl_root%': 'C:/OpenSSL-Win32'
              },
            }],
          ],
          'defines': [
            'uint=unsigned int',
          ],
          'libraries': [ 
            '-l<(openssl_root)/lib/libeay32.lib',
          ],
          'include_dirs': [
            '<(openssl_root)/include',
          ],
        }, { # OS!="win"
          'include_dirs': [
            # use node's bundled openssl headers on Unix platforms
            '<(node_root_dir)/deps/openssl/openssl/include'
          ],
        }],
      ],
    }
  ]
}
