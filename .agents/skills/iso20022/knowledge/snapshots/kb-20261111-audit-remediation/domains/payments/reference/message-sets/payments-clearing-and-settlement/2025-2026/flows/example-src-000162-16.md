---
template: false
document_kind: "business-flow"
title: "Foreign-exchange settlement chain — supplied example"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.009.001.13"]
message_families: ["pacs.009"]
source_locations: [{"source_id": "src-000162", "locator": "P2200–P2283; P2284–P2351; P2352–P2416"}]
flow_id: "flow-src-000162-example-16"
participant_ids: ["participant-src-000162-example-aaaafrpp", "participant-src-000162-example-bbbbittt", "participant-src-000162-example-ccccsess", "participant-src-000162-example-ddddlull", "participant-src-000162-example-ffffsess", "participant-src-000162-example-swedish-rtgs-system-rix-e7f1416"]
participants: ["participant-src-000162-example-aaaafrpp", "participant-src-000162-example-bbbbittt", "participant-src-000162-example-ccccsess", "participant-src-000162-example-ddddlull", "participant-src-000162-example-ffffsess", "participant-src-000162-example-swedish-rtgs-system-rix-e7f1416"]
issue_ids: ["issue-000059"]
limitations: ["This flow is the supplied historical example, not an invented scenario.", "Only source-defined outcomes and alternatives apply; the example does not separately specify formal preconditions or universal service rules."]
source_editions: ["March 2026"]
---

# Foreign-exchange settlement chain

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and source-defined conditions

**P2201** This example covers three FinancialInstitutionCreditTransfer messages.

**P2202** The first FinancialInstitutionCreditTransfer message is sent by AAAAFRPP to CCCCSESS.

**P2203** The second FinancialInstitutionCreditTransfer message is sent by CCCCSESS to FFFFSESS.

**P2204** The second FinancialInstitutionCreditTransfer message is sent by FFFFSESS to DDDDLULL.

**P2207** On 20 October 2015, AAAAFRPP agrees on a foreign exchange deal with BBBBITTT: 100 million SEK is sold against 10,621,575.00 EUR (exchange rate 9.4148). The deal is confirmed with common reference BBBBTT4148AAAAPP.

**P2208** On the same day AAAAFRPP sends a FinancialInstitutionCreditTransfer message to its SEK correspondent CCCCSESS. They instruct CCCCSESS to debit their account 123456789 with value date 22 October 2015 to pay 100 million SEK to BBBBITTT.

**P2209** BBBBITTT has communicated the following settlement instructions: the SEK amount is to be credited to the SEK sub- account of their account 995566ZZ876 with DDDDLULL. DDDDLULL owns a SEK account 24538877443 with FFFF Bank (FFFFSESS).

**P2211** The first FinancialInstitutionCreditTransfer message, from AAAAFRPP to CCCCSESS:

**P2286** On 22 October 2015 CCCC forwards the FinancialInstitutionCreditTransfer to the next party in the chain FFFF through the Swedish RTGS system RIX.

**P2288** The second FinancialInstitutionCreditTransfer message, from CCCCSESS to FFFFSESS:

**P2354** FFFF sends a FinancialInstitutionCreditTransfer to the next party which is the creditor agent DDDD, Luxemburg, for whom they service a SEK account. On receipt, DDDD will credit the SEK account of its client BBBBITTT.

**P2356** The third FinancialInstitutionCreditTransfer message, from FFFFSESS to DDDDLULL:


## Ordered message exchanges

| Step | Message | Sender / initiator | Receiver | Source evidence |
| --- | --- | --- | --- | --- |
| 16 | [pacs.009.001.13](../examples/example-16-pacs.009.001.13.md) | [AAAAFRPP](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaafrpp.md) | [CCCCSESS](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccsess.md) | P2213–P2283; T43 |
| 17 | [pacs.009.001.13](../examples/example-17-pacs.009.001.13.md) | [CCCCSESS](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccsess.md) | [FFFFSESS](../../../../../../../shared/reference/participants/participant-src-000162-example-ffffsess.md) | P2290–P2351; T44 |
| 18 | [pacs.009.001.13](../examples/example-18-pacs.009.001.13.md) | [FFFFSESS](../../../../../../../shared/reference/participants/participant-src-000162-example-ffffsess.md) | [DDDDLULL](../../../../../../../shared/reference/participants/participant-src-000162-example-ddddlull.md) | P2358–P2416; T45 |


## Participant roles and outcomes

| Participant | Instance fields / scope |
| --- | --- |
| [AAAAFRPP](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaafrpp.md) | Dbtr, InstgAgt |
| [BBBBITTT](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbittt.md) | Cdtr |
| [CCCCSESS](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccsess.md) | DbtrAgt, InstdAgt, InstgAgt |
| [DDDDLULL](../../../../../../../shared/reference/participants/participant-src-000162-example-ddddlull.md) | CdtrAgt, InstdAgt |
| [FFFFSESS](../../../../../../../shared/reference/participants/participant-src-000162-example-ffffsess.md) | InstdAgt, InstgAgt, IntrmyAgt1 |
| [Swedish RTGS system RIX](../../../../../../../shared/reference/participants/participant-src-000162-example-swedish-rtgs-system-rix-e7f1416.md) | clearing-system |


The narrative above supplies the responsible parties, accounting actions, decisions, charges and stated results. Message-instance participant fields retain their full paths; an institution may hold different functional roles in different relationships. No missing response, failure or formal postcondition is invented. These examples contain tables and XML instances rather than a separate reference diagram; the general process diagrams remain in [the source diagram index](../diagrams/clearing/index.md).

[Preserved source differences](../examples/source-discrepancies.md)
