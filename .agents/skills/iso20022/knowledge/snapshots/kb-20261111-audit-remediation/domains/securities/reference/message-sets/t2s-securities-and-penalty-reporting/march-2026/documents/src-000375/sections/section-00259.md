---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.1 FinancialInstrumentAttributes138", "7.1.12.1.40 FinancialInstrumentAttributeAdditionalDetails <FinInstrmAttrAddtlDtls>"]
file_pages: [336]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.1.40 FinancialInstrumentAttributeAdditionalDetails <FinInstrmAttrAddtlDtls>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 336 to 336.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 336

```text
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
7.1.12.1.40  FinancialInstrumentAttributeAdditionalDetails <FinInstrmAttrAddtlDtls>
Presence: [0..1]
Definition: Provides additional information about the financial instrument in narrative form.
Datatype: "Max350Text" on page 557
7.1.12.2  FinancialInstrument21
Definition: Security that is a sub-set of an investment fund, and is governed by the same investment
fund policy, for example, dividend option or valuation currency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassType <ClssTp> [0..1] Text 336
   SecuritiesForm <SctiesForm> [0..1] CodeSet 337
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 337
   ProductGroup <PdctGrp> [0..1] Text 337
   UmbrellaName <UmbrllNm> [0..1] Text 337
   BaseCurrency <BaseCcy> [0..1] CodeSet C1 337
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C1 338
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C2 338
   DualFundIndicator <DualFndInd> [0..1] Indicator 338
   CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C3 338
   RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C3 339
7.1.12.2.1  ClassType <ClssTp>
Presence: [0..1]
Definition: Features of units offered by a fund. For example, a unit may have a specific load structure,
for example, front end or back end, an income policy, eg, pay out or accumulate, or a trailer policy, eg,
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 336 March 2026
```

