---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.15 ChargesAccount <ChrgsAcct>"]
file_pages: [435]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.15 ChargesAccount <ChrgsAcct>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 435 to 435.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 435

```text
Datatype: "ChargeBearerType1Code" on page 588
CodeName Name Definition
DEBT BorneByDebtor All transaction charges are to be borne
by the debtor.
CRED BorneByCreditor All transaction charges are to be borne
by the creditor.
SHAR Shared In a credit transfer context, means that
transaction charges on the sender side
are to be borne by the debtor,
transaction charges on the receiver side
are to be borne by the creditor. In a
direct debit context, means that
transaction charges on the sender side
are to be borne by the creditor,
transaction charges on the receiver side
are to be borne by the debtor.
SLEV FollowingServiceLevel Charges are to be applied following the
rules agreed in the service level and/or
scheme.
5.4.2.15  ChargesAccount <ChrgsAcct>
Presence: [0..1]
Definition: Account used to process charges associated with a transaction.
Usage: Charges account should be used when charges have to be booked to an account different from
the account identified in debtor's account.
Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"
ChargesAccount <ChrgsAcct> contains the following elements (see "CashAccount40" on page 527
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 527
   Type <Tp> [0..1] ± 527
   Currency <Ccy> [0..1] CodeSet C2 528
   Name <Nm> [0..1] Text 528
   Proxy <Prxy> [0..1] ± 528
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 435 March 2026
```

