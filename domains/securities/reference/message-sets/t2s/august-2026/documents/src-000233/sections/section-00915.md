---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.2.2.44 Restriction <Rstrctn>", "28.4.2.1.2.2.44.1 EffectivePeriod <FctvPrd>"]
file_pages: [1341]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.2.44.1 EffectivePeriod <FctvPrd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1341 to 1341.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1341

```text
Restriction <Rstrctn> contains the following SecurityRestriction3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EffectivePeriod <FctvPrd> [0..1] ± 1341
   RestrictionType <RstrctnTp> [0..1]  1341
{Or     RestrictionType <RstrctnTp> [1..1] CodeSet 1342
Or}     ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1342
   LegalRestrictionType <LglRstrctnTp> [0..1]  1342
{Or     Code <Cd> [1..1] CodeSet 1342
Or}     Proprietary <Prtry> [1..1] ± 1343
   InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1343
{Or     Code <Cd> [1..1] CodeSet 1343
Or}     Proprietary <Prtry> [1..1] ± 1344
   InvestorType <InvstrTp> [0..*]  1344
{Or     Code <Cd> [1..1] CodeSet 1344
Or}     Proprietary <Prtry> [1..1] ± 1344
28.4.2.1.2.2.44.1  EffectivePeriod <FctvPrd>
Presence: [0..1]
Definition: Period during which the restriction applies.
EffectivePeriod <FctvPrd> contains the following elements (see "DateTimePeriod2" on page 2909 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2909
   ToDateTime <ToDtTm> [0..1] DateTime 2909
28.4.2.1.2.2.44.2  RestrictionType <RstrctnTp>
Presence: [0..1]
Definition: Type of the restriction, for example, selling restriction, buying restriction, placing restriction.
RestrictionType <RstrctnTp> contains one of the following SecurityRestrictionType2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RestrictionType <RstrctnTp> [1..1] CodeSet 1342
Or}   ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1342
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1341 August 2026
```

