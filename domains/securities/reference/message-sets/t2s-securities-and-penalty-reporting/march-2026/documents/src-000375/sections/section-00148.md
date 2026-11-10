---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.1 Identification <Id>", "6.4.6.11.4.1.3 ReallocationIdentification <RallcnId>", "6.4.6.11.4.1.3.2 Identification <Id>"]
file_pages: [212]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.1.3.2 Identification <Id>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 212 to 212.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 212

```text
Definition: Identification as assigned by the market infrastructure to the penalty and that is common for
both the failing and the non-failing participant.
Datatype: "Max35Text" on page 557
6.4.6.11.4.1.3.2  Identification <Id>
Presence: [0..1]
Definition: Identification as assigned by the market infrastructure to the penalty and that is the individual
identification of the penalty for the relevant account owner (that is either for the failing participant or for
the non failing participant).
Datatype: "Max35Text" on page 557
6.4.6.11.4.2  Type <Tp>
Presence: [1..1]
Definition: Type of the penalty.
Datatype: "PenaltyType1Code" on page 519
CodeName Name Definition
LMFP LateMatchingFailedPenalty Applies from the intended settlement
date until the matching date.
The penalty is charged to the participant
who was last to enter or modify the
relevant settlement instruction (for
example, "accepted timestamp" is later
than the one of the counterparty's
instruction) for the periods between the
intended settlement date and the day of
matching of the instruction.
SEFP SettlementFailedPenalty Penalties apply to instructions that fail to
settle on the intended settlement date. A
settlement instruction that "fails to settle
on that business day" must be
understood as a settlement instruction
that is not cancelled and remaining to be
settled, fully or partially, by the time of
the end of processing of the relevant cut-
off.
6.4.6.11.4.3  Insolvency <Inslvncy>
Presence: [0..1]
Definition: Party can no longer meet its financial obligations.
Usage: When indicator in not provided, the Insolvency is not relevant.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
6.4.6.11.4.4  Status <Sts>
Presence: [0..1]
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 212 March 2026
```

