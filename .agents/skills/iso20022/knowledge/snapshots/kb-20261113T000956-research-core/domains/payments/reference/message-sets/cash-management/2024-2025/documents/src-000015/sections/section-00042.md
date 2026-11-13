---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.9 CurrentBilateralLimit <CurBilLmt>", "3.4.2.1.2.1.9.1 CounterpartyIdentification <CtrPtyId>"]
file_pages: [72]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.9.1 CounterpartyIdentification <CtrPtyId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 72 to 72.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 72

```text
CurrentBilateralLimit <CurBilLmt> contains the following BilateralLimit4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CounterpartyIdentification <CtrPtyId> [1..1] ± 72
   LimitAmount <LmtAmt> [1..1] ± 73
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 73
   BilateralBalance <BilBal> [0..*]  73
     Amount <Amt> [1..1] Amount 73
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 74
     Type <Tp> [0..1]  74
{Or       Code <Cd> [1..1] CodeSet 74
Or}       Proprietary <Prtry> [1..1] Text 79
     Status <Sts> [0..1] CodeSet 80
     ValueDate <ValDt> [0..1] ± 80
     NumberOfPayments <NbOfPmts> [0..1] Quantity 80
3.4.2.1.2.1.9.1  CounterpartyIdentification <CtrPtyId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a member within a system, assigned using the
member identification scheme of the system.
CounterpartyIdentification <CtrPtyId> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 803 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  804
     BICFI <BICFI> [0..1] IdentifierSet C2 804
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 805
     LEI <LEI> [0..1] IdentifierSet 805
     Name <Nm> [0..1] Text 805
     PostalAddress <PstlAdr> [0..1] ± 805
     Other <Othr> [0..1] ± 806
   BranchIdentification <BrnchId> [0..1]  807
     Identification <Id> [0..1] Text 807
     LEI <LEI> [0..1] IdentifierSet 807
     Name <Nm> [0..1] Text 807
     PostalAddress <PstlAdr> [0..1] ± 807
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 72 February 2025
```

