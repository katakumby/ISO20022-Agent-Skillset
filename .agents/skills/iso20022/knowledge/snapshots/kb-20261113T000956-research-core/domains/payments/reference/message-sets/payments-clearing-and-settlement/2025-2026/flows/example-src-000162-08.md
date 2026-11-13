---
template: false
document_kind: "business-flow"
title: "Customer credit transfers, cover and relay — supplied example"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1259–P1392; P1393–P1567; P1568–P1671; P1672–P1793"}]
flow_id: "flow-src-000162-example-08"
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-aaaajpjt", "participant-src-000162-example-abc-corporation-51d6618", "participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-bbbbus66", "participant-src-000162-example-ccccjpjt", "participant-src-000162-example-ddddbebb", "participant-src-000162-example-def-electronics-bf4c618", "participant-src-000162-example-eeeedeff", "participant-src-000162-example-ghi-semiconductors-70a6ffe", "participant-src-000162-example-mr-jones-909aee6", "participant-src-000162-example-xyz-clearing-system-651b6a5", "participant-src-000162-example-zz-insurances-01c49f4"]
participants: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-aaaajpjt", "participant-src-000162-example-abc-corporation-51d6618", "participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-bbbbus66", "participant-src-000162-example-ccccjpjt", "participant-src-000162-example-ddddbebb", "participant-src-000162-example-def-electronics-bf4c618", "participant-src-000162-example-eeeedeff", "participant-src-000162-example-ghi-semiconductors-70a6ffe", "participant-src-000162-example-mr-jones-909aee6", "participant-src-000162-example-xyz-clearing-system-651b6a5", "participant-src-000162-example-zz-insurances-01c49f4"]
issue_ids: ["issue-000059"]
limitations: ["This flow is the supplied historical example, not an invented scenario.", "Only source-defined outcomes and alternatives apply; the example does not separately specify formal preconditions or universal service rules."]
source_editions: ["March 2026"]
---

# Customer credit transfers, cover and relay

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and source-defined conditions

**P1260** This example covers four FIToFICustomerCreditTransfer messages sent by BBBBUS33.

**P1261** The first FIToFICustomerCreditTransfer message is sent to AAAAGB2L.

**P1262** The second FIToFICustomerCreditTransfer message is sent to EEEEDEFF.

**P1263** The third FIToFICustomerCreditTransfer is sent to BBBBUS66

**P1264** A fourth FIToFICustomerCreditTransfer message, sent by EEEEDEFF to DDDDBEBB, is also shown.

**P1266** BBBB Bank, New York, has received a payment initiation from its client ABC Corporation, New York, that holds an account 00125574999 with them for payment of the following invoices:

**P1267** Invoice 1

**P1268** An invoice with number 4562, dated 08 September 2015 from DEF Electronics, London: 10 million JPY needs to be paid to DEF Electronics account 23683707994215 with AAAA Bank, London (AAAAGB2L). ABC Corporation assigns reference ABC/4562/2015-09-08 to the payment. Payment transaction charges are shared between ABC Corporation and DEF Electronics.

**P1269** Invoice 2

**P1270** An invoice with number ABC-13679, dated 15 September 2015 from GHI Semiconductors, Brussels: 500,000 EUR needs to be paid to GHI Semiconductors account BE30001216371411 with DDDD Bank, Belgium (DDDDBEBB). ABC Corporation assigns reference ABC/ABC-13679/2015-09-15 to the payment. The accounts receivable department of GHI Semiconductors needs to be advised when the funds have been credited to the account on telephone number +32/2/2222222. GHI Semiconductors will bear all payment transaction charges.

**P1271** Invoice 3

**P1272** An invoice with number 987-AC, dated 27 September 2015 from their branch ABC Corporation, California: 1 million USD needs to be paid on the branch account 4895623 with BBBB Bank, San Francisco (BBBBUS66). ABC assigns reference ABC/987-AC/2015-09-27 to the payment. Payment transaction charges are shared.

**P1274** ABC Corporation sent a CustomerCreditTransferInitiation message containing the 3 transactions to BBBB Bank. This is illustrated in the CustomerCreditTransferInitiation business example section of the Payments Initiation Message Reference Guide.

**P1275** To process the three payment instructions, BBBB Bank sends three FIToFICustomerCreditTransfer messages:

**P1276** A first message to AAAA Bank, London (AAAAGB2L). As the banks do not have a JPY account relationship, the payment is processed using the cover method. The JPY correspondent of BBBB Bank is CCCC Bank, Tokyo (CCCCJPJT). The JPY correspondent of AAAA Bank, London is AAAA Bank, Tokyo (AAAAJPJT). For the reimbursement instruction sent by BBBB Bank to its JPY correspondent CCCC Bank, please refer to the FinancialInstitutionCreditTransfer business example 1.

**P1277** A second message to its EUR correspondent EEEE Bank, Frankfurt (EEEEDEFF) where BBBB Bank has multiple accounts, for payment to DDDDBEBB. BBBB Bank specifies that account 29314569847 should be used for reimbursement.

**P1278** BBBB Bank has also received a payment order from their client Mr. Jones requesting to pay a 5 thousand EUR insurance premium by 30 September 2006 for contract ZZ/JO/164794 to ZZ Insurances, Frankfurt on their account DE89370400440532014000 with EEEEDEFF. Charges will be shared between the parties. BBBB Bank decides to include the latter 2 transactions in one FIToFICustomerCreditTransfer message.

**P1279** A third message is send to its branch BBBB Bank, San Francisco and instructs its branch to credit the account of ABC Corporation California in their books, account number 4895623.

**P1282** The first FIToFICustomerCreditTransfer message, from BBBBUS33 to AAAAGB2L:

**P1395** The second FIToFICustomerCreditTransfer, from BBBBUS33 to EEEEDEFF:

**P1570** The third FIToFICustomerCreditTransfer, from BBBBUS33 to BBBBUS66:

**P1674** On receipt of the message of BBBB Bank, EEEE Bank debits the account of BBBB Bank and credits its customer ZZ Insurances as instructed in the second payment transaction. EEEE Bank creates a new FIToFICustomerCreditTransfer to execute the first payment transaction and sends it to creditor agent DDDDBEBB through the clearing system XYZ of which both banks are members.

**P1676** FIToFICustomerCreditTransfer from EEEEDEFF to DDDDBEBB:


## Ordered message exchanges

| Step | Message | Sender / initiator | Receiver | Source evidence |
| --- | --- | --- | --- | --- |
| 8 | [pacs.008.001.14](../examples/example-08-pacs.008.001.14.md) | [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | P1284–P1392; T35 |
| 9 | [pacs.008.001.14](../examples/example-09-pacs.008.001.14.md) | [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | [EEEEDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-eeeedeff.md) | P1397–P1567; T36 |
| 10 | [pacs.008.001.14](../examples/example-10-pacs.008.001.14.md) | [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | [BBBBUS66](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus66.md) | P1572–P1671; T37 |
| 11 | [pacs.008.001.14](../examples/example-11-pacs.008.001.14.md) | [EEEEDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-eeeedeff.md) | [DDDDBEBB](../../../../../../../shared/reference/participants/participant-src-000162-example-ddddbebb.md) | P1678–P1793; T38 |


## Participant roles and outcomes

| Participant | Instance fields / scope |
| --- | --- |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | Cdtr, CdtrAgt, DbtrAgt, InstdAgt, InstgAgt |
| [AAAAJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaajpjt.md) | CdtrAgt, InstdAgt, InstdRmbrsmntAgt |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-51d6618.md) | Cdtr |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-875623a.md) | Dbtr, InitgPty |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | Agt, Dbtr, DbtrAgt, InstgAgt |
| [BBBBUS66](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus66.md) | CdtrAgt, InstdAgt |
| [CCCCJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccjpjt.md) | InstdAgt, InstgAgt, InstgRmbrsmntAgt |
| [DDDDBEBB](../../../../../../../shared/reference/participants/participant-src-000162-example-ddddbebb.md) | CdtrAgt, InstdAgt |
| [DEF Electronics](../../../../../../../shared/reference/participants/participant-src-000162-example-def-electronics-bf4c618.md) | Cdtr |
| [EEEEDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-eeeedeff.md) | Agt, CdtrAgt, InstdAgt, InstgAgt |
| [GHI Semiconductors](../../../../../../../shared/reference/participants/participant-src-000162-example-ghi-semiconductors-70a6ffe.md) | Cdtr |
| [Mr. Jones](../../../../../../../shared/reference/participants/participant-src-000162-example-mr-jones-909aee6.md) | Dbtr |
| [XYZ clearing system](../../../../../../../shared/reference/participants/participant-src-000162-example-xyz-clearing-system-651b6a5.md) | clearing-system |
| [ZZ Insurances](../../../../../../../shared/reference/participants/participant-src-000162-example-zz-insurances-01c49f4.md) | Cdtr |


The narrative above supplies the responsible parties, accounting actions, decisions, charges and stated results. Message-instance participant fields retain their full paths; an institution may hold different functional roles in different relationships. No missing response, failure or formal postcondition is invented. These examples contain tables and XML instances rather than a separate reference diagram; the general process diagrams remain in [the source diagram index](../diagrams/clearing/index.md).

[Preserved source differences](../examples/source-discrepancies.md)
