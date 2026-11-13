---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "16.4 Message Building Blocks", "16.4.7 Movements <Mvmnts>", "16.4.7.2 Movement <Mvmnt>", "16.4.7.2.10 SettlementAmount <SttlmAmt>"]
file_pages: [381]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 16.4.7.2.10 SettlementAmount <SttlmAmt>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 381 to 381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 381

```text
16.4.7.2.10  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Amount of money effectively settled and which will be credited to/debited from the account
owner's cash account. It may differ from the instructed settlement amount based on market tolerance
level.
SettlementAmount <SttlmAmt> contains one of the following elements (see "Amount2Choice" on
page 392 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 392
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C8 392
16.4.7.2.11  IntendedSettlementDate <IntnddSttlmDt>
Presence: [1..1]
Definition: Date and time at which the amount of money is intended to be moved.
IntendedSettlementDate <IntnddSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 398
Or}   DateTime <DtTm> [1..1] DateTime 398
16.4.7.2.12  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 493
16.4.7.2.13  CashSubBalanceIdentification <CshSubBalId>
Presence: [0..1]
Definition: Number identifying a lot constituting the sub-balance.
CashSubBalanceIdentification <CshSubBalId> contains the following elements (see
"GenericIdentification37" on page 408 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 408
   Issuer <Issr> [0..1] Text 408
16.4.7.2.14  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
381 March 2024
```

