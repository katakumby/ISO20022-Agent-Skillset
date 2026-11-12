---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.11 EventDeadlines <EvtDdlns>", "14.4.3.5.3.3.7.11.3 MarketDeadline <MktDdln>"]
file_pages: [790]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.11.3 MarketDeadline <MktDdln>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 790 to 790.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 790

```text
Definition: Date/time at which the account servicer has set as the deadline to respond, with instructions,
to an outstanding event. This time is dependent on the reference time zone of the account servicer as
specified in a Service Level Agreement (SLA).
ResponseDeadline <RspnDdln> contains one of the following elements (see "DateFormat44Choice"
on page 849 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 849
Or   DateCodeAndTime <DtCdAndTm> [1..1]  849
     DateCode <DtCd> [1..1]  850
{Or       Code <Cd> [1..1] CodeSet 850
Or}       Proprietary <Prtry> [1..1] ± 850
     Time <Tm> [1..1] Time 850
Or}   DateCode <DtCd> [1..1]  851
{Or     Code <Cd> [1..1] CodeSet 851
Or}     Proprietary <Prtry> [1..1] ± 851
14.4.3.5.3.3.7.11.3  MarketDeadline <MktDdln>
Presence: [0..1]
Definition: Issuer or issuer's agent deadline to respond with an instruction to an outstanding offer or
privilege.
MarketDeadline <MktDdln> contains one of the following elements (see "DateFormat43Choice" on
page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
14.4.3.5.3.3.7.11.4  ProtectDeadline <PrtctDdln>
Presence: [0..1]
Definition: Deadline for protect instructions.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 790 February 2026
```

