---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["10 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "10.4 Message Building Blocks", "10.4.5 RequestDetails <ReqDtls>", "10.4.5.1 Reference <Ref>", "10.4.5.1.5 PoolIdentification <PoolId>"]
file_pages: [160]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.072.001.02"]
---

# 10.4.5.1.5 PoolIdentification <PoolId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 160 to 160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 160

```text
Datatype: "Max35Text" on page 3328
10.4.5.1.5  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
10.4.5.2  Linkage <Lkg>
Presence: [0..1]
Definition: Specifies the type of linkage requested.
Linkage <Lkg> contains one of the following elements (see "LinkageType3Choice" on page 3056 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3056
Or}   Proprietary <Prtry> [1..1] ± 3057
10.4.5.3  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 2981 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 2981
Or}   Proprietary <Prtry> [1..1] ± 2981
10.4.5.4  OtherProcessing <OthrPrcg>
Presence: [0..*]
Definition: Specifies another type of processing change request.
OtherProcessing <OthrPrcg> contains the following elements (see "GenericIdentification30" on
page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
10.4.5.5  PartialSettlementIndicator <PrtlSttlmInd>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 160 August 2026
```

