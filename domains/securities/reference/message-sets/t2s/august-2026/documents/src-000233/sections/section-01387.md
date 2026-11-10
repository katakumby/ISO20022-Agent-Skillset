---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.42 Restriction <Rstrctn>", "32.4.3.1.1.3.42.1 EffectivePeriod <FctvPrd>"]
file_pages: [1996]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.42.1 EffectivePeriod <FctvPrd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1996 to 1996.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1996

```text
Restriction <Rstrctn> contains the following SecurityRestriction3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EffectivePeriod <FctvPrd> [0..1] ± 1996
   RestrictionType <RstrctnTp> [0..1]  1996
{Or     RestrictionType <RstrctnTp> [1..1] CodeSet 1997
Or}     ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1997
   LegalRestrictionType <LglRstrctnTp> [0..1]  1997
{Or     Code <Cd> [1..1] CodeSet 1997
Or}     Proprietary <Prtry> [1..1] ± 1998
   InvestorRestrictionType <InvstrRstrctnTp> [0..*]  1998
{Or     Code <Cd> [1..1] CodeSet 1998
Or}     Proprietary <Prtry> [1..1] ± 1999
   InvestorType <InvstrTp> [0..*]  1999
{Or     Code <Cd> [1..1] CodeSet 1999
Or}     Proprietary <Prtry> [1..1] ± 1999
32.4.3.1.1.3.42.1  EffectivePeriod <FctvPrd>
Presence: [0..1]
Definition: Period during which the restriction applies.
EffectivePeriod <FctvPrd> contains the following elements (see "DateTimePeriod2" on page 2909 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2909
   ToDateTime <ToDtTm> [0..1] DateTime 2909
32.4.3.1.1.3.42.2  RestrictionType <RstrctnTp>
Presence: [0..1]
Definition: Type of the restriction, for example, selling restriction, buying restriction, placing restriction.
RestrictionType <RstrctnTp> contains one of the following SecurityRestrictionType2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RestrictionType <RstrctnTp> [1..1] CodeSet 1997
Or}   ProprietaryRestriction <PrtryRstrctn> [1..1] ± 1997
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1996 August 2026
```

