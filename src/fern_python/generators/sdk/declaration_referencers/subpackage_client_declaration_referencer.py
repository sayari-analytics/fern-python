import fern.ir.resources as ir_types

from fern_python.codegen import Filepath

from .sdk_declaration_referencer import SdkDeclarationReferencer


class SubpackageClientDeclarationReferencer(SdkDeclarationReferencer[ir_types.Subpackage]):
    def get_filepath(self, *, name: ir_types.Subpackage) -> Filepath:
        return Filepath(
            directories=self._get_directories_for_fern_filepath(
                fern_filepath=name.fern_filepath,
            ),
            file=Filepath.FilepathPart(module_name="_client"),
        )

    def get_class_name(self, *, name: ir_types.Subpackage) -> str:
        return name.name.pascal_case.unsafe_name + "Client"
