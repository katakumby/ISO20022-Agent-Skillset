---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["23 camt.085.001.02 IntraBalanceMovementPendingReportV02", "23.4 Message Building Blocks", "23.4.7 Movements <Mvmnts>", "23.4.7.2 Movement <Mvmnt>", "23.4.7.2.10 SettlementAmount <SttlmAmt>"]
file_pages: [572]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 23.4.7.2.10 SettlementAmount <SttlmAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 572 to 572.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 572

```text
23.4.7.2.10  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Amount of money effectively settled and which will be credited to/debited from the account
owner's cash account. It may differ from the instructed settlement amount based on market tolerance
level.
SettlementAmount <SttlmAmt> contains one of the following elements (see "Amount2Choice" on
page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
23.4.7.2.11  IntendedSettlementDate <IntnddSttlmDt>
Presence: [1..1]
Definition: Date and time at which the amount of money is intended to be moved.
IntendedSettlementDate <IntnddSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
23.4.7.2.12  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 3320
23.4.7.2.13  CashSubBalanceIdentification <CshSubBalId>
Presence: [0..1]
Definition: Number identifying a lot constituting the sub-balance.
CashSubBalanceIdentification <CshSubBalId> contains the following elements (see
"GenericIdentification37" on page 2965 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
23.4.7.2.14  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities 572 August 2026
```

