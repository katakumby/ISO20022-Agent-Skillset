---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.1 Identification <Id>"]
file_pages: [2793]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.1 Identification <Id>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2793 to 2793.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2793

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       NumberOfEntries <NbOfNtries> [0..1] Quantity 2827
81.4.6.11.4.1  Identification <Id>
Presence: [1..1]
Definition: Identification as assigned to the penalty by the market infrastructure.
Identification <Id> contains the following PenaltyIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] Text 2793
   Identification <Id> [0..1] Text 2793
   ReallocationIdentification <RallcnId> [0..1]  2793
     MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] Text 2793
     Identification <Id> [0..1] Text 2794
81.4.6.11.4.1.1  MarketInfrastructureIdentification <MktInfrstrctrId>
Presence: [1..1]
Definition: Identification as assigned by the market infrastructure to the penalty and that is common for
both the failing and the non-failing participant.
Datatype: "Max35Text" on page 3328
81.4.6.11.4.1.2  Identification <Id>
Presence: [0..1]
Definition: Identification as assigned by the market infrastructure to the penalty and that is the individual
identification of the penalty for the relevant account owner (that is either for the failing participant or for
the non failing participant).
Datatype: "Max35Text" on page 3328
81.4.6.11.4.1.3  ReallocationIdentification <RallcnId>
Presence: [0..1]
Definition: Identification as assigned to the penalty by the market infrastructure following a reallocation.
ReallocationIdentification <RallcnId> contains the following PenaltyIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] Text 2793
   Identification <Id> [0..1] Text 2794
81.4.6.11.4.1.3.1  MarketInfrastructureIdentification <MktInfrstrctrId>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2793 August 2026
```

