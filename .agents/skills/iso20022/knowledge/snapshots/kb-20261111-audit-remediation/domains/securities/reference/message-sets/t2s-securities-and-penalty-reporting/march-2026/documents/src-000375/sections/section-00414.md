---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.44 PenaltyStatus2Code"]
file_pages: [518]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.44 PenaltyStatus2Code

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 518 to 518.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 518

```text
CodeName Name Definition
CURR Current To report the new penalties and the
modified penalties in one single
message /report.
FWAM ForwardAmend To report a penalty list that has been
amended (that is the penalty list contains
only updated and/or removed penalties
that have already been previously
reported in a FWIS Penalty List).
FWIS ForwardInitialSubmission To report a daily penalty list created for
the first time (that is the penalty list
contains only newly computed penalties)
7.2.2.44  PenaltyStatus2Code
Definition: Specifies the status of the penalty.
Type: CodeSet
CodeName Name Definition
ACTV Active Penalty is active for the party.
NCOM NotComputed Penalty could not be computed.
REMO Removed Removal of a cash penalty where
settlement cannot be performed for
reasons that are independent from any
of the CSD participants or the CSD.
7.2.2.45  PenaltyStatusReason2Code
Definition: Specifies the reason for the status of the penalty.
Type: CodeSet
CodeName Name Definition
UPDT Updated Penalty has been updated.
SUSP TradingSuspended Penalty was removed becuase of ISIN
suspension from trading.
TECH TechnicalImpossibilities Penalty was removed becuase there
were thecnical imposssibilities at the
CSD level that prevent settlement, such
as: a failure of the infrastructure
components, a cyber-attack, network
problems.
SWIC Switched Penalty has been switched between the
failing and non-failing party.
SESU SettlementSuspended Penalty was removed becuase of ISIN
suspension from settlement due to a
reconciliation issue under Article 65 (2)
and (6) of the RTS on CSD
Requirements.
SEMP SettlementOnMultiplePlatforms Settlement on multiple platforms where
one of the platforms is closed for
settlement (either cash or securities).
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 518 March 2026
```

