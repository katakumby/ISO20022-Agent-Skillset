---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.4 FinancialInstrument21", "82.1.13.4.1 ClassType <ClssTp>"]
file_pages: [2948]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.4.1 ClassType <ClssTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2948 to 2948.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2948

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassType <ClssTp> [0..1] Text 2948
   SecuritiesForm <SctiesForm> [0..1] CodeSet 2948
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2948
   ProductGroup <PdctGrp> [0..1] Text 2949
   UmbrellaName <UmbrllNm> [0..1] Text 2949
   BaseCurrency <BaseCcy> [0..1] CodeSet C1 2949
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C1 2949
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C1 2950
   DualFundIndicator <DualFndInd> [0..1] Indicator 2950
   CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C3 2950
   RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C3 2950
82.1.13.4.1  ClassType <ClssTp>
Presence: [0..1]
Definition: Features of units offered by a fund. For example, a unit may have a specific load structure,
for example, front end or back end, an income policy, eg, pay out or accumulate, or a trailer policy, eg,
with or without. Fund classes are typically denoted by a single character, for example, 'Class A', 'Class
2'.
Datatype: "Max35Text" on page 3328
82.1.13.4.2  SecuritiesForm <SctiesForm>
Presence: [0..1]
Definition: Specifies the form, that is, ownership, of the security.
Datatype: "FormOfSecurity1Code" on page 3254
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
82.1.13.4.3  DistributionPolicy <DstrbtnPlcy>
Presence: [0..1]
Definition: Income policy relating to a class type, that is, if income is paid out or retained in the fund.
Datatype: "DistributionPolicy1Code" on page 3236
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2948 August 2026
```

