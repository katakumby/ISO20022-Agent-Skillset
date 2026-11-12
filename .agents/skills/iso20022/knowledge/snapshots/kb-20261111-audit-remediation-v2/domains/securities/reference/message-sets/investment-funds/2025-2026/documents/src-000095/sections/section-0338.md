---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 2"]
content_origin: "source-transcription"
---

# SecuritiesBalanceTransparencyReport semt.041.001.02 Message 2

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Transparency Of Holdings / SecuritiesBalanceTransparencyReport semt.041.001.02 Message 2.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5826** SecuritiesBalanceTransparencyReport semt.041.001.02 Message 2

**P5827** Message 2 from the above diagram

**P5828** Description

**P5829** ICSD (ICSDLULL), having received a SecuritiesBalanceTransparencyReport message from CUSA (CUSALULL), with the details of CUSA’s three customer accounts, sends a SecuritiesBalanceTransparencyReport message back to CUSA. 

**P5830** [1]	The data is enriched with the place where the securities are held. The securities are held at TRAG, account 111111. (In the message, this is specified at safekeeping account level.)

**P5831** [2]	For account CUSA1111, the data is enriched with the holding and balance information. The holding is ISIN LU1234567890, the aggregated settled balance is 600 units and the aggregated traded balance is 640 units. (In the message, this is specified at account sub level 1.)

**P5832** [3]	In addition, the account data provided in the message received (message 1 in the flow) is echoed back and enriched with agent code information for CUSA’s underlying customer accounts:

**P5833** CUSA’s three clients account and holdings: 

**P5834**  [1.1]	Client AAXX (AAXXLULL), account AAXX-c1. For ISIN LU1234567890, the aggregated settled balance is 90 units, the aggregated traded balance is 100 units. 

**P5835** The agent code for this client for this holding is 77777, issued by TRAGLULL, the role is distributor.

**P5836** (In the message, this is specified at account sub level 2 repetition 1.)

**P5837** [1.2]	Client AAYY (AAYYLULL), account AAYY-c2. For ISIN LU1234567890, the aggregated settled balance is 110 units, the aggregated traded balance is 120 units. 

**P5838** The agent code for this client for this holding is AGNTLULL, a distributor.

**P5839** (In the message, this is specified at account sub level 2 repetition 2.)

**P5840** [1.3]	Client AAZZ (AAZZLULL), account AAZZ-c3. For ISIN LU1234567890, the aggregated settled balance is 400 units, the traded balance is 420 units. 

**P5841** The agent for this client for this holding is DISTLULL, a distributor.

**P5842** (In the message, this is specified at account sub level 2 repetition 3.)

**P5843** Message Instance 

[T62 - complete table](../tables/tbl-0062.md)

**P5846**   


**P5847** Diagrammatic Overview

**P5848** This diagram represents a simplified view of the safekeeping account sequence with sub level 1 and sub level 2 account sequences from the xml message above.

[fig-0145 - original figure evidence](../diagrams/fig-0145.md)

