---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 1"]
content_origin: "source-transcription"
---

# FIToFICustomerCreditTransfer pacs.008.001.14 - 1

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Business Examples / FIToFICustomerCreditTransfer pacs.008.001.14 - 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1259** FIToFICustomerCreditTransfer pacs.008.001.14 - 1

**P1260** This example covers four FIToFICustomerCreditTransfer messages sent by BBBBUS33. 

**P1261** The first FIToFICustomerCreditTransfer message is sent to AAAAGB2L. 

**P1262** The second FIToFICustomerCreditTransfer message is sent to EEEEDEFF. 

**P1263** The third FIToFICustomerCreditTransfer is sent to BBBBUS66

**P1264** A fourth FIToFICustomerCreditTransfer message, sent by EEEEDEFF to DDDDBEBB, is also shown.

**P1265** Description

**P1266** BBBB Bank, New York, has received a payment initiation from its client ABC Corporation, New York, that holds an account 00125574999 with them for payment of the following invoices:

**P1267** Invoice 1

**P1268** An invoice with number 4562, dated 08 September 2015 from DEF Electronics, London: 10 million JPY needs to be paid to DEF Electronics account 23683707994215 with AAAA Bank, London (AAAAGB2L). ABC Corporation assigns reference ABC/4562/2015-09-08 to the payment. Payment transaction charges are shared between ABC Corporation and DEF Electronics.

**P1269** Invoice 2

**P1270** An invoice with number ABC-13679, dated 15 September 2015 from GHI Semiconductors, Brussels: 500,000 EUR needs to be paid to GHI Semiconductors account BE30001216371411 with DDDD Bank, Belgium (DDDDBEBB). ABC Corporation assigns reference ABC/ABC-13679/2015-09-15 to the payment. The accounts receivable department of GHI Semiconductors needs to be advised when the funds have been credited to the account on telephone number +32/2/2222222. GHI Semiconductors will bear all payment transaction charges.

**P1271** Invoice 3

**P1272** An invoice with number 987-AC, dated 27 September 2015 from their branch ABC Corporation, California: 1 million USD needs to be paid on the branch account 4895623 with BBBB Bank, San Francisco (BBBBUS66). ABC assigns reference ABC/987-AC/2015-09-27 to the payment. Payment transaction charges are shared.

**P1273** Related Message Examples

**P1274** ABC Corporation sent a CustomerCreditTransferInitiation message containing the 3 transactions to BBBB Bank. This is illustrated in the CustomerCreditTransferInitiation business example section of the Payments Initiation Message Reference Guide.

**P1275** To process the three payment instructions, BBBB Bank sends three FIToFICustomerCreditTransfer messages:

**P1276** A first message to AAAA Bank, London (AAAAGB2L). As the banks do not have a JPY account relationship, the payment is processed using the cover method. The JPY correspondent of BBBB Bank is CCCC Bank, Tokyo (CCCCJPJT). The JPY correspondent of AAAA Bank, London is AAAA Bank, Tokyo (AAAAJPJT). For the reimbursement instruction sent by BBBB Bank to its JPY correspondent CCCC Bank, please refer to the FinancialInstitutionCreditTransfer business example 1.

**P1277** A second message to its EUR correspondent EEEE Bank, Frankfurt (EEEEDEFF) where BBBB Bank has multiple accounts, for payment to DDDDBEBB. BBBB Bank specifies that account 29314569847 should be used for reimbursement.

**P1278** BBBB Bank has also received a payment order from their client Mr. Jones requesting to pay a 5 thousand EUR insurance premium by 30 September 2006 for contract ZZ/JO/164794 to ZZ Insurances, Frankfurt on their account DE89370400440532014000 with EEEEDEFF. Charges will be shared between the parties. BBBB Bank decides to include the latter 2 transactions in one FIToFICustomerCreditTransfer message.

**P1279** A third message is send to its branch BBBB Bank, San Francisco and instructs its branch to credit the account of ABC Corporation California in their books, account number 4895623.

