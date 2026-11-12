---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Functionality"]
content_origin: "source-transcription"
---

# Functionality

Source: [src-000353](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`. Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Functionality.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P72** Functionality

**P73** The Collateral Management Reference Data messages definitions are specifically designed to support the following technical functions:

**P74** Collateral Value Creation Request: the reda.024 is sent by CBs, payment banks, external collateral management systems for instructing the creation of a securities valuation by providing details about the securities valuation to be created.

**P75** Eligible Securities Creation Request: the reda.025 is sent by CBs, payment banks or any party authorised by them for defining a security as eligible for auto-collateralisation or client-collateralisation by providing details about the security to be defined as eligible.

**P76** Eligible Counterpart CSD Creation Request: the reda.026 is sent by CSDs or any party authorised by them to and it is used for defining a CSD as eligible counterpart CSD by providing details about the CSD to be defined as eligible counterpart CSD.

**P77** Close Link Creation Request: the reda.027 is sent by CBs, external collateral management systems or payment banks for instructing the creation of a close link by providing details about the close link to be created.

**P78** Eligible Securities Deletion Request: the reda.075 is sent by CBs, payment banks or any party authorised by them to remove the eligibility of a security that has lost its eligibility status for auto-collateralisation or client-collateralisation by providing details about the security to be defined as no longer eligible.

**P79** Close Link Deletion Request: the reda.077 is sent by CBs, external collateral management systems or payment banks for instructing the deletion of a close link by providing details about the close link to be deleted.

**P80** Collateral Data Status Advice: the reda.028 is sent to inform the sender of the originating request about the status of a collateral data maintenance request. It is the answer message to: reda.024, reda.025, reda.027, reda.075, reda.077.

**P81** This message is sent in the following message usages: rejected, queued and completed.

**P82** Eligible Counterpart CSD Status Advice: the reda.044 is sent to inform the sender of the originating request about the status of an eligible counterpart CSD maintenance request. It is the answer message to reda.026.

**P83** This message is sent in the following message usages: rejected, queued and completed.

**P85** See Message Definition Report Part 2 for the message and formats.

