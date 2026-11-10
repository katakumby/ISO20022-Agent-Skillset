---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.44 Restriction <Rstrctn>", "27.4.2.3.44.1 EffectivePeriod <FctvPrd>"]
file_pages: [792]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.44.1 EffectivePeriod <FctvPrd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 792 to 792.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 792

```text
Restriction <Rstrctn> contains the following SecurityRestriction3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EffectivePeriod <FctvPrd> [0..1] ± 792
   RestrictionType <RstrctnTp> [0..1]  792
{Or     RestrictionType <RstrctnTp> [1..1] CodeSet 793
Or}     ProprietaryRestriction <PrtryRstrctn> [1..1] ± 793
   LegalRestrictionType <LglRstrctnTp> [0..1]  793
{Or     Code <Cd> [1..1] CodeSet 793
Or}     Proprietary <Prtry> [1..1] ± 794
   InvestorRestrictionType <InvstrRstrctnTp> [0..*]  794
{Or     Code <Cd> [1..1] CodeSet 794
Or}     Proprietary <Prtry> [1..1] ± 795
   InvestorType <InvstrTp> [0..*]  795
{Or     Code <Cd> [1..1] CodeSet 795
Or}     Proprietary <Prtry> [1..1] ± 795
27.4.2.3.44.1  EffectivePeriod <FctvPrd>
Presence: [0..1]
Definition: Period during which the restriction applies.
EffectivePeriod <FctvPrd> contains the following elements (see "DateTimePeriod2" on page 2909 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2909
   ToDateTime <ToDtTm> [0..1] DateTime 2909
27.4.2.3.44.2  RestrictionType <RstrctnTp>
Presence: [0..1]
Definition: Type of the restriction, for example, selling restriction, buying restriction, placing restriction.
RestrictionType <RstrctnTp> contains one of the following SecurityRestrictionType2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RestrictionType <RstrctnTp> [1..1] CodeSet 793
Or}   ProprietaryRestriction <PrtryRstrctn> [1..1] ± 793
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 792 August 2026
```

