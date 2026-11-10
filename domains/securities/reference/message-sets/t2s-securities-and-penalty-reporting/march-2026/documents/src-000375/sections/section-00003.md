---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [3, 4]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01", "semt.026.001.01", "semt.027.001.01", "semt.040.001.01", "semt.044.001.01"]
---

# 1 Message Set Overview

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 3 to 4.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Securities and Penalty Reporting message set. It
includes the new query and responses messages related to Securities and Penalty reporting as well as
the Penalties Report MessageDefinitions that have been developed in the scope of the Target2-
Securities Business Justification (See BJ#042) approved by the Securities SEG on 19 February 2025.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
semt.025.001.01
SecuritiesAccountPositionQueryV01
The SecuritiesAccountPositionQuery message is sent
by an account owner to an account servicer or
servicing party to request an account view on the
position at a particular point in time period, or during a
particular time period, where all positions are
summarised in the account structure that is compatible
with the query.
Usage:
The message may also be used to:
-re-send a message previously sent (the sub-function
of the message is Duplicate),
- provide a third party with a copy of a message for
information (the sub-function of the message is Copy),
-re-send to a third party a copy of a message for
information (the sub-function of the message is
CopyDuplicate).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
The SecuritiesSettlementInstructionQuery message is
sent from an account owner/requestor to a settlement
infrastructure.
The message is used to query information on the
securities settlement instructions, that satisfy the
defined selection criteria.
semt.027.001.01
SecuritiesSettlementTransactionQueryRespons
eV01
The SecuritiesSettlementResponse message is sent
from a settlement infrastructure to an account owner/
requestor to provide the details of the securities
settlement instructions, as selected in the search
criteria defined in the request.
semt.040.001.01
SecuritiesAccountPositionResponseV01
The SecuritiesAccountPositionResponse message is
sent by a market infrastructure to an instructing party to
report the securities positions for the given date period
as requested in the query, for all securities across all
accounts satisfying the query criteria.
Approved by the Securities SEG 19 February 2026. Message Set Overview
Target2-Securities - Securities and Penalty Reporting 3 March 2026
```

## File page 4

```text
MessageDefinition Definition
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
The SecuritiesTransactionPenaltiesReport V01
message is sent by the Executing/Servicing Party to
the instructing party to inform about the cash penalties:
- Newly computed cash penalties. For example, in
case of a CSD, the information shall include the cash
penalties that are either imposed or credited to all of its
participants and the CSD itself; in case of a CSD
participant, the information shall include the cash
penalties that are either imposed or credited to the
CSD participant itself.
- Modified penalties: to inform about the modifications
occurred in existing cash penalties since the previous
reporting.
- Aggregated amounts of cash penalties: to inform
about the aggregated amounts of the cash penalties
computed for the business days of a given period, for
example the previous month.
Approved by the Securities SEG 19 February 2026. Message Set Overview
Target2-Securities - Securities and Penalty Reporting 4 March 2026
```

