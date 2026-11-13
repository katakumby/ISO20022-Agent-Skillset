---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.5 AccountEntry <AcctNtry>", "5.4.2.1.3.2.1.5.1 Account <Acct>"]
file_pages: [316]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.5.1 Account <Acct>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 316 to 316.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 316

```text
AccountEntry <AcctNtry> contains the following CashAccountAndEntry5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Account <Acct> [1..1]  C14,
C13
316
     Identification <Id> [0..1] ± 317
     Type <Tp> [0..1] ± 317
     Currency <Ccy> [0..1] CodeSet C2 317
     Name <Nm> [0..1] Text 318
     Proxy <Prxy> [0..1] ± 318
     Owner <Ownr> [0..1] ± 318
     Servicer <Svcr> [0..1] ± 319
   Entry <Ntry> [0..1]  320
     Amount <Amt> [0..1] Amount C1, C9 320
     Date <Dt> [0..1] ± 321
     Status <Sts> [0..1] CodeSet 321
     Identification <Id> [0..1] Text 322
     StatementIdentification <StmtId> [0..1] Text 322
     AccountServicerReference <AcctSvcrRef> [0..1] Quantity 322
     AdditionalEntryInformation <AddtlNtryInf> [0..*] Text 322
5.4.2.1.3.2.1.5.1  Account <Acct>
Presence: [1..1]
Definition: Account to or from which a cash entry is made.
Impacted by: C14 "IdentificationOrProxyPresenceRule", C13 "IdentificationAndProxyGuideline"
Account <Acct> contains the following CashAccount43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 317
   Type <Tp> [0..1] ± 317
   Currency <Ccy> [0..1] CodeSet C2 317
   Name <Nm> [0..1] Text 318
   Proxy <Prxy> [0..1] ± 318
   Owner <Ownr> [0..1] ± 318
   Servicer <Svcr> [0..1] ± 319
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 316 February 2025
```

