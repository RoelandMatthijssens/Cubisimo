""" """

from unittest import TestSuite, TextTestRunner, main

from unittest_block import suite as blockSuite
from unittest_blockType import suite as blockTypeSuite
from unittest_blockTypeKeeper import suite as blockTypeKeeperSuite
from unittest_config import suite as configSuite
from unittest_defaultConfig import suite as defaultConfigSuite
from unittest_encoder import suite as encoderSuite
from unittest_chunkGenerator import suite as chunkGeneratorSuite
from unittest_fileObject import suite as fileObjectSuite

suite = TestSuite()
suite.addTest( blockSuite )
suite.addTest( blockTypeSuite )
suite.addTest( blockTypeKeeperSuite )
suite.addTest( configSuite )
suite.addTest( defaultConfigSuite )
suite.addTest( encoderSuite )
suite.addTest( chunkGeneratorSuite )
suite.addTest( fileObjectSuite )
# suite.addTest( Suite )

if __name__ == '__main__':
	TextTestRunner(verbosity=1).run( suite )
