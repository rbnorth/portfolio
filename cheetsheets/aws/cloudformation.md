## <ins>CloudFormation</ins>

Usefual links:

[AWS CloudFromation](https://aws.amazon.com/cloudformation/)

[AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/)
    
[AWS CloudFormation Templates](https://aws.amazon.com/cloudformation/resources/templates/)  

### Anatomy of a CloudFormation Template

[Template Anatomy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html)

**Anatomy Example:**

```yaml
AWSTemplateFormatVersion: "version date"

Description:
  String

Metadata:
  template metadata

Parameters:
  set of parameters

Mappings:
  set of mappings

Conditions:
  set of conditions

Transform:
  set of transforms

Resources:
  set of resources

Outputs:
  set of outputs
```
**Reference:**

[Format Version (optional)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/format-version-structure.html)

[Description (optional)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-description-structure.html)

[Metadata (optional)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html)

[Parameters (optional)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html)

[Mappings (optional)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html)

[Conditions (optional)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/conditions-section-structure.html)

[Transform (optional)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-section-structure.html)

[Resources (required)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html)

[Outputs (optional)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html)

**Intrinsic Functions:**

!Ref

!GetAtt

!FindInMap

!Sub

!Join

!Equals

### Nested Stackes



