---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope", "Functionality"]
content_origin: "source-transcription"
---

# Functionality

Source: [src-000365](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Locator: heading path Scope and Functionality / Scope / Functionality.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P54** Functionality

**P55** The Link Reference Data message definitions are specifically designed to support the following technical functions:

**P57** the Security CSD Link Creation Request (reda.045) provides a user, granted with the appropriate rights, with the possibility to create a link between a financial instrument and a CSD in their system.

**P58** This functionality is available to an authorised party, who must provide specific information, such as the financial instrument identification, the Issuer or Investor CSD identification, technical issuer identification, whether that CSD is responsible for the security maintenance, issuance account identification, as well as the start and the end date for the validity of the link, in order to link a financial instrument to a CSD.

**P59** The Security CSD Link Maintenance Request (reda.046) provides a user, granted with the appropriate rights, with the possibility to update an existing Security CSD Link. 

**P60** This functionality is available to all authorised parties. 

**P62** The Security CSD Link Status Advice (reda.047) informs the Instructing Party about the lifecycle of the creation or the modification of the link, using the following statuses:

**P63** Rejected

**P64** The Creation or Maintenance Request did not pass validation, some reasons could be:

**P65** - the mandatory information is not present or incorrect,

**P66** - the instruction is not a new occurrence,

**P67** - the Instructing Party or the user do not have the rights to create a Security CSD link,

**P68** - the instruction has already been received and is being processed. 

**P69** It is possible to have more than one reason for the rejection status.

**P70** Queued 

**P71** The processing of the Security CSD Link Creation Request or maintenance request has been delayed. 

**P72** Completed

**P73** The instruction or maintenance has been successfully processed.

**P75** The Account Link Creation Request (reda.049) provides a user, granted with the appropriate rights, with the possibility to create a link between a Cash Account and a Securities Account.

**P76** This functionality is available to an authorised party, who must provide specific information, such as the identification of the securities account and the dedicated cash account, whether the account link is set as default:

**P77** for settlement, 

**P78** for auto-collateralisation usage, 

**P79** for settlement of cash legs

**P80** the request must also specify the start and end date for the Account link validity.

**P82** The Account Link Maintenance Request (reda.050) provides a user, granted with the appropriate rights, with the possibility to update an existing Account Link.

**P83** This functionality is available to all authorised parties.

**P85** The Account Link Status Advice (reda.051) informs the Instructing Party about the lifecycle of the Account link creation request or maintenance request, with following statuses:

**P86** Rejected

**P87** The instruction did not pass validation, some reasons could be:

**P88** - the mandatory information is not present or incorrect,

**P89** - the instruction is not a new occurrence,

**P90** - the Instructing Party do not have the rights to create an Account Link, 

**P91** - the instruction has already been received and is being processed. 

**P92** It is possible to have more than one reason for the rejection status.

**P93** Queued 

**P94** The processing of the Account link Creation Request or maintenance request has been delayed. 

**P95** Completed

**P96** The link request or maintenance has been successfully processed.

**P97**   
See Message Definition Report Part 2 for the message and formats.

