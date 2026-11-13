---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "6.4 Message Building Blocks", "6.4.6 RequestDetails <ReqDtls>", "6.4.6.1 Reference <Ref>", "6.4.6.1.5 PoolIdentification <PoolId>"]
file_pages: [102]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 6.4.6.1.5 PoolIdentification <PoolId>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 102 to 102.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 102

```text
Datatype: "Max35Text" on page 497
6.4.6.1.5  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 497
6.4.6.2  Linkage <Lkg>
Presence: [0..1]
Definition: Specifies the type of linkage requested.
Linkage <Lkg> contains one of the following elements (see "LinkageType3Choice" on page 413 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 413
Or}   Proprietary <Prtry> [1..1] ± 414
6.4.6.3  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 414 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 414
Or}   Proprietary <Prtry> [1..1] ± 414
6.4.6.4  OtherProcessing <OthrPrcg>
Presence: [0..*]
Definition: Specifies another type of processing change request.
OtherProcessing <OthrPrcg> contains the following elements (see "GenericIdentification30" on
page 409 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
6.4.6.5  PartialSettlementIndicator <PrtlSttlmInd>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
102 March 2024
```

