---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "8.4 Message Building Blocks", "8.4.5 CashAccount <CshAcct>"]
file_pages: [140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 8.4.5 CashAccount <CshAcct>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 140 to 140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 140

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus69Choice" on page 452 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 453
Or   Rejected <Rjctd> [1..1] ± 453
Or   Repair <Rpr> [1..1] ± 453
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 454
Or   Proprietary <Prtry> [1..1] ± 454
Or   Denied <Dnd> [1..1] ± 454
Or}   Cancelled <Canc> [1..1] ± 455
8.4.5 CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which an entry is made.
Impacted by: C12 "IdentificationOrProxyPresenceRule", C11 "IdentificationAndProxyGuideline"
CashAccount <CshAcct> contains the following elements (see "CashAccount40" on page 387 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 388
   Type <Tp> [0..1] ± 388
   Currency <Ccy> [0..1] CodeSet C2 388
   Name <Nm> [0..1] Text 389
   Proxy <Prxy> [0..1] ± 389
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
8.4.6 CashAccountOwner <CshAcctOwnr>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
140 March 2024
```

