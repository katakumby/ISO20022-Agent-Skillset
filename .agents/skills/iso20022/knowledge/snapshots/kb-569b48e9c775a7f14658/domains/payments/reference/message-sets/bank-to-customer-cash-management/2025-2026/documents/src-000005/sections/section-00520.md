---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.24 UnderlyingAllocation <UndrlygAllcn>", "4.4.2.14.18.2.24.3 Account <Acct>"]
file_pages: [749]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.24.3 Account <Acct>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 749 to 749.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 749

```text
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
4.4.2.14.18.2.24.3  Account <Acct>
Presence: [1..1]
Definition: Unambiguous identification of the account to which the allocation is due or from.
Impacted by: C19 "IdentificationOrProxyPresenceRule", C17 "IdentificationAndProxyGuideline"
Account <Acct> contains the following elements (see "CashAccount40" on page 796 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 796
   Type <Tp> [0..1] ± 796
   Currency <Ccy> [0..1] CodeSet C1 797
   Name <Nm> [0..1] Text 797
   Proxy <Prxy> [0..1] ± 797
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
4.4.2.14.18.2.24.4  Purpose <Purp>
Presence: [1..1]
Definition: Underlying reason for the allocation.
Usage: This applies to the allocation only, this is not the underlying reason for the payment.
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 851 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 851
Or}   Proprietary <Prtry> [1..1] Text 851
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
749 March 2026
```

