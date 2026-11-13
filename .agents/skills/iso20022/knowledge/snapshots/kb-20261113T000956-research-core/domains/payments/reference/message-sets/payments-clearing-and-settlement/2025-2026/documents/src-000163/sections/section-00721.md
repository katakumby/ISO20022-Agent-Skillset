---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.7 GarnishmentRemittance <GrnshmtRmt>", "7.4.2.40.30.2.7.1 Type <Tp>"]
file_pages: [977]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.7.1 Type <Tp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 977 to 977.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 977

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  977
     CodeOrProprietary <CdOrPrtry> [1..1]  977
{Or       Code <Cd> [1..1] CodeSet 978
Or}       Proprietary <Prtry> [1..1] Text 978
     Issuer <Issr> [0..1] Text 978
   Garnishee <Grnshee> [0..1] ± 978
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 979
   ReferenceNumber <RefNb> [0..1] Text 980
   Date <Dt> [0..1] Date 981
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C9 981
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 981
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 981
7.4.2.40.30.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  977
{Or     Code <Cd> [1..1] CodeSet 978
Or}     Proprietary <Prtry> [1..1] Text 978
   Issuer <Issr> [0..1] Text 978
7.4.2.40.30.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 978
Or}   Proprietary <Prtry> [1..1] Text 978
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
977 March 2026
```

