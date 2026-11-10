---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01", "56.3 Constraints"]
file_pages: [2242]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.036.001.01"]
---

# 56.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2242 to 2242.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2242

```text
56.3 Constraints
C1 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
56.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
56.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
56.4.2 SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to be used to query the securities account audit trail by the executing
system.
SearchCriteria <SchCrit> contains the following SecuritiesAccountAuditTrailSearchCriteria3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccountIdentification <SctiesAcctId> [0..1] ± 2242
   DatePeriod <DtPrd> [0..1]  2243
{Or     FromDate <FrDt> [1..1] Date 2243
Or     ToDate <ToDt> [1..1] Date 2243
Or     FromToDate <FrToDt> [1..1] ± 2243
Or     EqualDate <EQDt> [1..1] Date 2244
Or}     NotEqualDate <NEQDt> [1..1] Date 2244
56.4.2.1  SecuritiesAccountIdentification <SctiesAcctId>
Presence: [0..1]
Definition: Unique identification of the securities account to be queried.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
Target2-Securities 2242 August 2026
```

