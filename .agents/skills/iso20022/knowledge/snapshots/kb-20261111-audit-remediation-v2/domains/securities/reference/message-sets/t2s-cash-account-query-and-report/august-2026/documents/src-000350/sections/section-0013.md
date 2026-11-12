---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Functionality"]
content_origin: "source-transcription"
---

# Functionality

Source: [src-000350](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Functionality.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P78** Functionality

**P79** These Cash Account Query and Report messages definitions are specifically designed to support the following technical functions:

**P80** Account Query List: the acmt.025 is sent to make the following types of queries:

**P81** Cash Account Reference Data Query enabling the sender to request the detailed reference data of a cash account;

**P82** Cash Account List Query enabling the sender to request a list of cash accounts ;

**P83** Settlement Bank Account Group Query enabling the sender to request details of Settlement Bank Account groups.

**P85** Account List Report: the acmt.026  is sent to provide with a list of accounts with the following features:

**P86** Detailed reference data information;

**P87** Cash account identifiers;

**P88** Settlement bank account groups identification and composition;

**P89** The AccountListReport message is sent as response to the AccountQueryList acmt.025 message, containing information on requested items (cash accounts or settlement bank account groups) or business error reports.

**P91** Cash Account Activity Advice: the reda.038  is sent to provide with a list of detailed information on:

**P92** Creation of new cash accounts

**P93** Modification  of already existing cash accounts

**P94** Deletion of already existing cash accounts;

**P95** The CashAccountActivityAdvice is sent in push mode to the subscribing parties. Elements in the activity advice vary depending on the requestor scope.

**P97** Cash Account Audit Trail Query: the reda.039  is sent to make the following types of queries:

**P98** Detailed audit trail information on cash accounts over a period of time;

**P100** Cash Account Audit Trail Report: the reda.040  is sent to provide with the following detailed information:

**P101** Creation of new cash accounts

**P102** Modification of already existing cash accounts

**P103** Deletion of already existitng cash accounts

**P104** The CashAccountAuditTrailReport message is sent as response to the CashAccountAuditTrailQuery reda.039 message, containing information on requested items or business error reports.

**P106** See Message Definition Report Part 2 for the message and formats.

