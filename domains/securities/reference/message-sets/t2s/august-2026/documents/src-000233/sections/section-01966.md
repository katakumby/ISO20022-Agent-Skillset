---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.7 Underlying <Undrlyg>", "76.4.3.4.7.2 SettlementTransaction <SttlmTx>", "76.4.3.4.7.2.4 TradeDate <TradDt>"]
file_pages: [2686]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.7.2.4 TradeDate <TradDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2686 to 2686.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2686

```text
76.4.3.4.7.2.4  TradeDate <TradDt>
Presence: [0..1]
Definition: Specifies the date/time on which the trade was executed.
TradeDate <TradDt> contains one of the following elements (see "TradeDate8Choice" on page 2910
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 2910
Or}   DateCode <DtCd> [1..1]  2910
{Or     Code <Cd> [1..1] CodeSet 2910
Or}     Proprietary <Prtry> [1..1] ± 2911
76.4.3.4.7.2.5  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
SettlementDate <SttlmDt> contains one of the following elements (see "SettlementDate17Choice" on
page 2912 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 2912
Or}   DateCode <DtCd> [1..1] ± 2912
76.4.3.4.7.2.6  DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of delivering settlement parties.
Impacted by: C18 "Party2PresenceRule", C19 "Party3PresenceRule", C20 "Party4PresenceRule", C21
"Party5PresenceRule"
DeliveringSettlementParties <DlvrgSttlmPties> contains the following elements (see
"SettlementParties78" on page 3115 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 3115
   Party1 <Pty1> [0..1] ± 3116
   Party2 <Pty2> [0..1] ± 3116
   Party3 <Pty3> [0..1] ± 3117
   Party4 <Pty4> [0..1] ± 3117
   Party5 <Pty5> [0..1] ± 3117
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2686 August 2026
```

