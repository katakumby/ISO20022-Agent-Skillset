---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.9 RelatedParties <RltdPties>", "2.4.2.15.18.2.9.1 InitiatingParty <InitgPty>"]
file_pages: [133]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.9.1 InitiatingParty <InitgPty>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 133 to 133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 133

```text
RelatedParties <RltdPties> contains the following TransactionParties12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InitiatingParty <InitgPty> [0..1]  133
{Or     Party <Pty> [1..1] ± 134
Or}     Agent <Agt> [1..1] ± 135
   Debtor <Dbtr> [0..1]  136
{Or     Party <Pty> [1..1] ± 136
Or}     Agent <Agt> [1..1] ± 137
   DebtorAccount <DbtrAcct> [0..1] ± C20,
C18
138
   UltimateDebtor <UltmtDbtr> [0..1]  139
{Or     Party <Pty> [1..1] ± 139
Or}     Agent <Agt> [1..1] ± 140
   Creditor <Cdtr> [0..1]  141
{Or     Party <Pty> [1..1] ± 141
Or}     Agent <Agt> [1..1] ± 142
   CreditorAccount <CdtrAcct> [0..1] ± C20,
C18
143
   UltimateCreditor <UltmtCdtr> [0..1]  144
{Or     Party <Pty> [1..1] ± 144
Or}     Agent <Agt> [1..1] ± 145
   TradingParty <TradgPty> [0..1]  146
{Or     Party <Pty> [1..1] ± 146
Or}     Agent <Agt> [1..1] ± 147
   Proprietary <Prtry> [0..*]  148
     Type <Tp> [1..1] Text 148
     Party <Pty> [1..1]  148
{Or       Party <Pty> [1..1] ± 149
Or}       Agent <Agt> [1..1] ± 150
2.4.2.15.18.2.9.1  InitiatingParty <InitgPty>
Presence: [0..1]
Definition: Party that initiated the payment that is reported in the entry.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
133 March 2026
```

