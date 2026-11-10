---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.10 OptionProtectInstructionBalance <OptnPrtctInstrBal>"]
file_pages: [789]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.10 OptionProtectInstructionBalance <OptnPrtctInstrBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 789 to 789.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 789

```text
14.4.3.5.3.3.7.10  OptionProtectInstructionBalance <OptnPrtctInstrBal>
Presence: [0..1]
Definition: Daily total of all protect instructions for a given option.
OptionProtectInstructionBalance <OptnPrtctInstrBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.3.7.11  EventDeadlines <EvtDdlns>
Presence: [1..1]
Definition: Provides information about the deadlines related to a corporate action option.
EventDeadlines <EvtDdlns> contains the following CorporateActionEventDeadlines3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EarlyResponseDeadline <EarlyRspnDdln> [0..1] ± 789
   ResponseDeadline <RspnDdln> [0..1] ± 789
   MarketDeadline <MktDdln> [0..1] ± 790
   ProtectDeadline <PrtctDdln> [0..1] ± 790
   CoverProtectDeadline <CoverPrtctDdln> [0..1] ± 791
14.4.3.5.3.3.7.11.1  EarlyResponseDeadline <EarlyRspnDdln>
Presence: [0..1]
Definition: Date/time that the account servicer has set as the deadline to respond, with instructions, to
an outstanding event, giving the holder eligibility to incentives. This time is dependent on the reference
time zone of the account servicer as specified in a Service Level Agreement (SLA).
EarlyResponseDeadline <EarlyRspnDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
14.4.3.5.3.3.7.11.2  ResponseDeadline <RspnDdln>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 789 February 2026
```

