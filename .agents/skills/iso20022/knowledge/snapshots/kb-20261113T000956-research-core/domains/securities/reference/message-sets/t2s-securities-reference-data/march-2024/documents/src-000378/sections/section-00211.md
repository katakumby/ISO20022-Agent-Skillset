---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.44 Restriction <Rstrctn>", "13.1.6.2.44.1 EffectivePeriod <FctvPrd>"]
file_pages: [289]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.44.1 EffectivePeriod <FctvPrd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 289 to 289.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 289

```text
Restriction <Rstrctn> contains the following SecurityRestriction3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EffectivePeriod <FctvPrd> [0..1] ± 289
   RestrictionType <RstrctnTp> [0..1]  289
{Or     RestrictionType <RstrctnTp> [1..1] CodeSet 290
Or}     ProprietaryRestriction <PrtryRstrctn> [1..1] ± 290
   LegalRestrictionType <LglRstrctnTp> [0..1]  290
{Or     Code <Cd> [1..1] CodeSet 290
Or}     Proprietary <Prtry> [1..1] ± 291
   InvestorRestrictionType <InvstrRstrctnTp> [0..*]  291
{Or     Code <Cd> [1..1] CodeSet 291
Or}     Proprietary <Prtry> [1..1] ± 292
   InvestorType <InvstrTp> [0..*]  292
{Or     Code <Cd> [1..1] CodeSet 292
Or}     Proprietary <Prtry> [1..1] ± 292
13.1.6.2.44.1  EffectivePeriod <FctvPrd>
Presence: [0..1]
Definition: Period during which the restriction applies.
EffectivePeriod <FctvPrd> contains the following elements (see "DateTimePeriod2" on page 236 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 236
   ToDateTime <ToDtTm> [0..1] DateTime 236
13.1.6.2.44.2  RestrictionType <RstrctnTp>
Presence: [0..1]
Definition: Type of the restriction, for example, selling restriction, buying restriction, placing restriction.
RestrictionType <RstrctnTp> contains one of the following SecurityRestrictionType2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RestrictionType <RstrctnTp> [1..1] CodeSet 290
Or}   ProprietaryRestriction <PrtryRstrctn> [1..1] ± 290
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 289 March 2024
```

