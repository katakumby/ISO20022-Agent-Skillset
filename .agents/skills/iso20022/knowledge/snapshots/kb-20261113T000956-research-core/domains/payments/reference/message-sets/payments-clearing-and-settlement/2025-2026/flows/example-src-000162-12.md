---
template: false
document_kind: "business-flow"
title: "Centralised invoice payment — supplied example"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1794–P1907; P1908–P2027"}]
flow_id: "flow-src-000162-example-12"
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-bbbbie2d", "participant-src-000162-example-biogenetics-crops-f41cbcd", "participant-src-000162-example-biogenetics-hq-918607e", "participant-src-000162-example-ccccie2d", "participant-src-000162-example-irish-rtgs-system-37a0513", "participant-src-000162-example-seed-inc-21a3af5"]
participants: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-bbbbie2d", "participant-src-000162-example-biogenetics-crops-f41cbcd", "participant-src-000162-example-biogenetics-hq-918607e", "participant-src-000162-example-ccccie2d", "participant-src-000162-example-irish-rtgs-system-37a0513", "participant-src-000162-example-seed-inc-21a3af5"]
issue_ids: ["issue-000059"]
limitations: ["This flow is the supplied historical example, not an invented scenario.", "Only source-defined outcomes and alternatives apply; the example does not separately specify formal preconditions or universal service rules."]
source_editions: ["March 2026"]
---

# Centralised invoice payment

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and source-defined conditions

**P1795** This example covers two FIToFICustomerCreditTransfer messages. The first FIToFICustomerCreditTransfer message is sent by AAAA Bank to BBBB Bank. The second FIToFICustomerCreditTransfer message is sent by BBBB Bank to CCCC Bank.

**P1798** Biogenetics-Crops, Glasgow, subsidiary of Biogenetics HQ, London, has received an invoice with number SX-25T, dated 13 October 2010 from Seed Inc., Dublin: 75 thousand EUR needs to be paid to the account of Seed Inc. IE29CCCC93115212345678 held at CCCC Bank, Dublin (CCCCIE2D). Transaction charges for the payment are shared between Biogenetics and Seed Inc.

**P1799** The payment of all Biogenetics invoices is centralised at Biogenetics HQ. It assigns reference CROPS/SX-25T/

**P1800** 2015-10-13 to the payment order and passes it on to AAAA Bank (AAAAGB2L) where it holds the account

**P1801** 46373892034012. AAAA Bank sends the payment to its correspondent BBBB Bank in Dublin (BBBBIE2D).

**P1803** The first FIToFICustomerCreditTransfer, sent by AAAA Bank to BBBB Bank:

**P1910** On receipt of the payment instruction, BBBB Bank debits AAAA Bank account, deducts its processing charges and sends an FIToFICustomerCreditTransfer to CCCC Bank, Dublin across the Irish RTGS system.

**P1912** The second FIToFICustomerCreditTransfer, sent by BBBB Bank to CCCC Bank:


## Ordered message exchanges

| Step | Message | Sender / initiator | Receiver | Source evidence |
| --- | --- | --- | --- | --- |
| 12 | [pacs.008.001.14](../examples/example-12-pacs.008.001.14.md) | [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | P1805–P1907; T39 |
| 13 | [pacs.008.001.14](../examples/example-13-pacs.008.001.14.md) | [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | [CCCCIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccie2d.md) | P1914–P2027; T40 |


## Participant roles and outcomes

| Participant | Instance fields / scope |
| --- | --- |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | Cdtr, CdtrAgt, DbtrAgt, InstdAgt, InstgAgt |
| [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | Agt, InstdAgt, InstgAgt |
| [Biogenetics - CROPS](../../../../../../../shared/reference/participants/participant-src-000162-example-biogenetics-crops-f41cbcd.md) | UltmtDbtr |
| [Biogenetics - HQ](../../../../../../../shared/reference/participants/participant-src-000162-example-biogenetics-hq-918607e.md) | Dbtr |
| [CCCCIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccie2d.md) | Agt, CdtrAgt, InstdAgt, InstgAgt |
| [Irish RTGS system](../../../../../../../shared/reference/participants/participant-src-000162-example-irish-rtgs-system-37a0513.md) | clearing-system |
| [Seed Inc.](../../../../../../../shared/reference/participants/participant-src-000162-example-seed-inc-21a3af5.md) | Cdtr |


The narrative above supplies the responsible parties, accounting actions, decisions, charges and stated results. Message-instance participant fields retain their full paths; an institution may hold different functional roles in different relationships. No missing response, failure or formal postcondition is invented. These examples contain tables and XML instances rather than a separate reference diagram; the general process diagrams remain in [the source diagram index](../diagrams/clearing/index.md).

[Preserved source differences](../examples/source-discrepancies.md)
