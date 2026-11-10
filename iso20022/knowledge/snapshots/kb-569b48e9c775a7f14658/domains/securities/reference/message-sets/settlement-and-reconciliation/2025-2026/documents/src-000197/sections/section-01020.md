---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.3 FinancialInstrument21", "35.1.11.3.1 ClassType <ClssTp>"]
file_pages: [1458]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.3.1 ClassType <ClssTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1458 to 1458.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1458

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassType <ClssTp> [0..1] Text 1458
   SecuritiesForm <SctiesForm> [0..1] CodeSet 1458
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 1458
   ProductGroup <PdctGrp> [0..1] Text 1459
   UmbrellaName <UmbrllNm> [0..1] Text 1459
   BaseCurrency <BaseCcy> [0..1] CodeSet C1 1459
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C1 1459
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C2 1460
   DualFundIndicator <DualFndInd> [0..1] Indicator 1460
   CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C7 1460
   RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C7 1460
35.1.11.3.1  ClassType <ClssTp>
Presence: [0..1]
Definition: Features of units offered by a fund. For example, a unit may have a specific load structure,
for example, front end or back end, an income policy, eg, pay out or accumulate, or a trailer policy, eg,
with or without. Fund classes are typically denoted by a single character, for example, 'Class A', 'Class
2'.
Datatype: "Max35Text" on page 2192
35.1.11.3.2  SecuritiesForm <SctiesForm>
Presence: [0..1]
Definition: Specifies the form, that is, ownership, of the security.
Datatype: "FormOfSecurity1Code" on page 2079
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
35.1.11.3.3  DistributionPolicy <DstrbtnPlcy>
Presence: [0..1]
Definition: Income policy relating to a class type, that is, if income is paid out or retained in the fund.
Datatype: "DistributionPolicy1Code" on page 2061
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1458 March 2026
```

