---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.1 Identification <Id>", "81.4.6.11.4.1.3 ReallocationIdentification <RallcnId>", "81.4.6.11.4.1.3.2 Identification <Id>"]
file_pages: [2794]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.1.3.2 Identification <Id>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2794 to 2794.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2794

```text
Definition: Identification as assigned by the market infrastructure to the penalty and that is common for
both the failing and the non-failing participant.
Datatype: "Max35Text" on page 3328
81.4.6.11.4.1.3.2  Identification <Id>
Presence: [0..1]
Definition: Identification as assigned by the market infrastructure to the penalty and that is the individual
identification of the penalty for the relevant account owner (that is either for the failing participant or for
the non failing participant).
Datatype: "Max35Text" on page 3328
81.4.6.11.4.2  Type <Tp>
Presence: [1..1]
Definition: Type of the penalty.
Datatype: "PenaltyType1Code" on page 3269
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
81.4.6.11.4.3  Insolvency <Inslvncy>
Presence: [0..1]
Definition: Party can no longer meet its financial obligations.
Usage: When indicator in not provided, the Insolvency is not relevant.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
81.4.6.11.4.4  Status <Sts>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2794 August 2026
```

