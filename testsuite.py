""" """

import sys
sys.path.append( 'src/' )

from unittest import TestSuite, TextTestRunner, main

from testing.fileObject import suite as fileObjectSuite
from testing.config import suite as configSuite
from testing.defaultConfig import suite as defaultConfigSuite
from testing.baseBlock import suite as baseBlockSuite
from testing.blockType import suite as blockTypeSuite
from testing.blockTypeFactory import suite as blockTypeFactorySuite
from testing.encoder import suite as encoderSuite
from testing.chunkGenerator import suite as chunkGeneratorSuite
from testing.chunk import suite as chunkSuite

suite = TestSuite()
suite.addTest( fileObjectSuite )
suite.addTest( configSuite )
suite.addTest( defaultConfigSuite )
suite.addTest( baseBlockSuite )
suite.addTest( blockTypeSuite )
suite.addTest( blockTypeFactorySuite )
suite.addTest( encoderSuite )
suite.addTest( chunkGeneratorSuite )
suite.addTest( chunkSuite )
# suite.addTest( Suite )

if __name__ == '__main__':
	TextTestRunner(verbosity=1).run( suite )
