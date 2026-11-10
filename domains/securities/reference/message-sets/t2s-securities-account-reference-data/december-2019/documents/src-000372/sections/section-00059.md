---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01", "9.3 Constraints"]
file_pages: [65]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.036.001.01"]
---

# 9.3 Constraints

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 65 to 65.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 65

```text
9.3 Constraints
C1 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
9.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
9.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 82 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 82
   CreationDateTime <CreDtTm> [0..1] DateTime 82
9.4.2 SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to be used to query the securities account audit trail by the executing
system.
SearchCriteria <SchCrit> contains the following SecuritiesAccountAuditTrailSearchCriteria3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccountIdentification <SctiesAcctId> [0..1] ± 65
   DatePeriod <DtPrd> [0..1]  66
{Or     FromDate <FrDt> [1..1] Date 66
Or     ToDate <ToDt> [1..1] Date 66
Or     FromToDate <FrToDt> [1..1] ± 66
Or     EqualDate <EQDt> [1..1] Date 67
Or}     NotEqualDate <NEQDt> [1..1] Date 67
9.4.2.1  SecuritiesAccountIdentification <SctiesAcctId>
Presence: [0..1]
Definition: Unique identification of the securities account to be queried.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
Target2-Securities - Securities Account Reference Data 65 December 2019
```

