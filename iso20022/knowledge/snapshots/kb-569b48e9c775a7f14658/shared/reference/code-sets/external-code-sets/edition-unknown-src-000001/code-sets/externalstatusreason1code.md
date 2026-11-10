---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalStatusReason1Code"]
code_set: "ExternalStatusReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalStatusReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalStatusReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the status reason, as published in an external status reason code list.
External code sets can be downloaded from www.iso20022.org.
*`AB01`-Clearing process aborted due to timeout.
*`AB02`-Clearing process aborted due to a fatal error.   
*`AB03`-Settlement aborted due to timeout.   
*`AB04`-Settlement process aborted due to a fatal error.   
*`AB05`-Transaction stopped due to timeout at the Creditor Agent.
*`AB06`-Transaction stopped due to timeout at the Instructed Agent.
*`AB07`-Agent of message is not online.
Generic usage if it cannot be determined who exactly is not online.
*`AB08`-Creditor Agent is not online.
*`AB09`-Transaction stopped due to error at the Creditor Agent.
*`AB10`-Transaction stopped due to error at the Instructed Agent.
*`AB11`-Transaction stopped due to timeout at the Debtor Agent.
*`AC01`-Account number is invalid or missing.   

*`AC02`-Debtor account number invalid or missing
*`AC03`-Creditor account number invalid or missing
*`AC04`-Account number specified has been closed on the bank of account's books.
*`AC05`-Debtor account number closed.
*`AC06`-Account specified is blocked, prohibiting posting of transactions against it.
*`AC07`-Creditor account number closed
*`AC08`-Branch code is invalid or missing
*`AC09`-Account currency is invalid or missing
*`AC10`-Debtor account currency is invalid or missing
*`AC11`-Creditor account currency is invalid or missing
*`AC12`-Account type missing or invalid.
Generic usage if cannot specify between group and payment information levels
*`AC13`-Debtor account type missing or invalid
*`AC14`-Creditor account type missing or invalid
*`AC15`-The account details for the counterparty have changed.
*`AC16`-Credit or debit card number is invalid.
*`AG01`-Transaction forbidden on this type of account (formerly NoAgreement)
*`AG02`-Bank Operation code specified in the message is not valid for receiver
*`AG03`-Transaction type not supported/authorized on this account.
*`AG04`-Agent country code is missing or invalid.
Generic usage if cannot specify between group and payment information levels.
*`AG05`-Debtor agent country code is missing or invalid
*`AG06`-Creditor agent country code is missing or invalid
*`AG07`-Debtor account cannot be debited for a generic reason.
Code value may be used in general purposes and as a replacement for AM04 if debtor bank does not reveal its customer's insufficient funds for privacy reasons
*`AG08`-Transaction failed due to invalid or missing user or access right
*`AG09`-Original payment never received.
*`AG10`-Agent of message is suspended from the Real Time Payment system.
Generic usage if it cannot be determined who exactly is suspended.
*`AG11`-Creditor Agent of message is suspended from the Real Time Payment system.
*`AG12`-Payment orders made by transferring funds from one account to another at the same financial institution (bank or payment institution) are not allowed.
*`AG13`-Returned payments derived from previously returned transactions are not allowed.
*`AGNT`-Agent in the payment workflow is incorrect
*`AM01`-Specified message amount is equal to zero
*`AM02`-Specific transaction/message amount is greater than allowed maximum
*`AM03`-Specified message amount is an non processable currency outside of existing agreement
*`AM04`-Amount of funds available to cover specified message amount is insufficient.
*`AM05`-Duplication
*`AM06`-Specified transaction amount is less than agreed minimum.
*`AM07`-Amount specified in message has been blocked by regulatory authorities.
*`AM09`-Amount received is not the amount agreed or expected
*`AM10`-Sum of instructed amounts does not equal the control sum.
*`AM11`-Transaction currency is invalid or missing
*`AM12`-Amount is invalid or missing
*`AM13`-Transaction amount exceeds limits set by clearing system
*`AM14`-Transaction amount exceeds limits agreed between bank and client
*`AM15`-Transaction amount below minimum set by clearing system
*`AM16`-Control Sum at the Group level is invalid
*`AM17`-Control Sum at the Payment Information level is invalid
*`AM18`-Number of transactions is invalid or missing.
Generic usage if cannot specify between group and payment information levels.
*`AM19`-Number of transactions at the Group level is invalid or missing
*`AM20`-Number of transactions at the Payment Information level is invalid
*`AM21`-Transaction amount exceeds limits agreed between bank and client.
*`AM22`-Unable to apply zero amount to designated account. For example, where the rules of a service allow the use of zero amount payments, however the back-office system is unable to apply the funds to the account. If the rules of a service prohibit the use of zero amount payments, then code AM01 is used to report the error condition.
*`AM23`-Transaction amount exceeds settlement limit.
*`BE01`-Identification of end customer is not consistent with associated account number. (formerly CreditorConsistency).
*`BE04`-Specification of creditor's address, which is required for payment, is missing/not correct (formerly IncorrectCreditorAddress).
*`BE05`-Party who initiated the message is not recognised by the end customer
*`BE06`-End customer specified is not known at associated Sort/National Bank Code or does no longer exist in the books
*`BE07`-Specification of debtor's address, which is required for payment, is missing/not correct.
*`BE08`-Debtor name is missing
*`BE09`-Country code is missing or Invalid.
Generic usage if cannot specifically identify debtor or creditor
*`BE10`-Debtor country code is missing or invalid
*`BE11`-Creditor country code is missing or invalid
*`BE12`-Country code of residence is missing or Invalid.
Generic usage if cannot specifically identify debtor or creditor
*`BE13`-Country code of debtor's residence is missing or Invalid
*`BE14`-Country code of creditor's residence is missing or Invalid
*`BE15`-Identification code missing or invalid.
Generic usage if cannot specifically identify debtor or creditor.
*`BE16`-Debtor or Ultimate Debtor identification code missing or invalid
*`BE17`-Creditor or Ultimate Creditor identification code missing or invalid
*`BE18`-Contact details missing or invalid
*`BE19`-Charge bearer code for transaction type is invalid
*`BE20`-Name length exceeds local rules for payment type.
*`BE21`-Name missing or invalid.  Generic usage if cannot specifically identify debtor or creditor.
*`BE22`-Creditor name is missing
*`BE23`-Phone number or email address, or any other proxy, used as the account proxy is unknown or invalid.
*`CERI`-Credit transfer is not tagged as an Extended Remittance Information (ERI) transaction but contains ERI.
*`CH03`-Value in Requested Execution Date or Requested Collection Date is too far in the future
*`CH04`-Value in Requested Execution Date or Requested Collection Date is too far in the past
*`CH07`-Element is not to be used at B- and C-Level
*`CH09`-Mandate changes are not allowed
*`CH10`-Information on mandate changes are missing
*`CH11`-Value in Creditor Identifier is incorrect
*`CH12`-Creditor Identifier is ambiguous at Transaction Level
*`CH13`-Original Debtor Account is not to be used
*`CH14`-Original Debtor Agent  is not to be used
*`CH15`-Content Remittance Information/Structured includes more than 140 characters
*`CH16`-Content is incorrect
*`CH17`-Element is not allowed
*`CH19`-Values in Interbank Settlement Date or Requested Collection Date will be set to the next TARGET day
*`CH20`-Number of decimal points not compatible with the currency
*`CH21`-Mandatory element is missing.
*`CH22`-SDD CORE and B2B not permitted within one message.
*`CHQC`-Cheque has been presented in cheque clearing and settled on the creditor’s account.
*`CNOR`-Creditor bank is not registered under this BIC in the CSM
*`CURR`-Currency of the payment is incorrect
*`CUST`-Cancellation requested by the Debtor
*`DNOR`-Debtor bank is not registered under this BIC in the CSM
*`DS01`-The electronic signature(s) is/are correct
*`DS02`-An authorized user has cancelled the order
*`DS03`-The user’s attempt to cancel the order was not successful.
*`DS04`-The order was rejected by the bank side (for reasons concerning content)
*`DS05`-The order was correct and could be forwarded for postprocessing
*`DS06`-The order was transferred to VEU
*`DS07`-All actions concerning the order could be done by the EBICS bank server
*`DS08`-The decompression of the file was not successful
*`DS09`-The decryption of the file was not successful
*`DS0A`-Data signature is required.
*`DS0B`-Data signature for the format is not available or invalid.
*`DS0C`-The signer certificate is revoked.
*`DS0D`-The signer certificate is not valid (revoked or not active).
*`DS0E`-The signer certificate is not present.
*`DS0F`-The authority of the signer certification sending the certificate is unknown.
*`DS0G`-Signer is not allowed to sign this operation type.
*`DS0H`-Signer is not allowed to sign for this account.
*`DS0K`-The number of transaction is over the number allowed for this signer.
*`DS10`-The certificate is revoked for the first signer.
*`DS11`-The certificate is not valid (revoked or not active) for the first signer.
*`DS12`-The certificate is not present for the first signer.
*`DS13`-The authority of signer certification sending the certificate is unknown for the first signer.
*`DS14`-The user is unknown on the server
*`DS15`-The same signature has already been sent to the bank
*`DS16`-The public key version is not correct. This code is returned when a customer sends signature files to the financial institution after conversion from an older program version (old ES format) to a new program version (new ES format) without having carried out re-initialisation with regard to a public key change.
*`DS17`-Order data and signatures don’t match
*`DS18`-File cannot be tested, the complete order has to be repeated. This code is returned in the event of a malfunction during the signature check, e.g. not enough storage space.
*`DS19`-The user’s rights (concerning his signature) are insufficient to execute the order
*`DS20`-The certificate is revoked for the second signer.
*`DS21`-The certificate is not valid (revoked or not active) for the second signer.
*`DS22`-The certificate is not present for the second signer.
*`DS23`-The authority of signer certification sending the certificate is unknown for the second signer.
*`DS24`-Waiting time expired due to incomplete order
*`DS25`-The order file was deleted by the bank server 
(for multiple reasons)
*`DS26`-The same user has signed multiple times
*`DS27`-The user is not yet activated (technically)
*`DT01`-Invalid date (eg, wrong or missing settlement date)
*`DT02`-Invalid creation date and time in Group Header (eg, historic date)
*`DT03`-Invalid non bank processing date (eg, weekend or local public holiday)
*`DT04`-Future date not supported
*`DT05`-Associated message, payment information block or transaction was received after agreed processing cut-off date, i.e., date in the past.
*`DT06`-Execution Date has been modified in order for transaction to be processed
*`DU01`-Message Identification is not unique.
*`DU02`-Payment Information Block is not unique.
*`DU03`-Transaction is not unique.
*`DU04`-End To End ID is not unique.
*`DU05`-Instruction ID is not unique.
*`DUPL`-Payment or charge is a duplicate of another payment or charge.
*`ED01`-Correspondent bank not possible.
*`ED03`-Balance of payments complementary info is requested
*`ED05`-Settlement of the transaction has failed.
*`ED06`-Interbank settlement system not available.
*`ERIN`-Extended Remittance Information (ERI) option is not supported.
*`FF01`-File Format incomplete or invalid
*`FF02`-Syntax error reason is provided as narrative information in the additional reason information.
*`FF03`-Payment Type Information is missing or invalid.
Generic usage if cannot specify Service Level or Local Instrument code
*`FF04`-Service Level code is missing or invalid
*`FF05`-Local Instrument code is missing or invalid
*`FF06`-Category Purpose code is missing or invalid
*`FF07`-Purpose is missing or invalid
*`FF08`-End to End Id missing or invalid
*`FF09`-Cheque number missing or invalid
*`FF10`-File or transaction cannot be processed due to technical issues at the bank side
*`FF11`-Clearing request rejected due it being subject to an abort operation.
*`G000`-In an FI To FI Customer Credit Transfer: The Status Originator transferred the payment to the next Agent or to a Market Infrastructure. The payment transfer is tracked. No further updates will follow from the Status Originator.

In a Financial Institution Credit Transfer with cover: The Status Originator performed the account booking and transferred the cover transaction to the next Reimbursement Agent or to a Market Infrastructure. The payment transfer is tracked. No further updates will follow from the Status Originator.

*`G001`-In an FI To FI Customer Credit Transfer: The Status Originator transferred the payment to the next Agent or to a Market Infrastructure. The payment transfer is not tracked. No further updates will follow from the Status Originator.

In a Financial Institution Credit Transfer with cover: The Status Originator performed the account booking and transferred the cover transaction to the next Reimbursement Agent or to a Market Infrastructure. The payment transfer is not tracked. No further updates will follow from the Status Originator.

*`G002`-In a FIToFI Customer Credit Transfer: Credit to the creditor’s account may not be confirmed same day. Update will follow from the Status Originator.
In a Financial Institution Credit Transfer with cover: Debit/credit to nostro account may not be confirmed same day or Financial Institution Credit Transfer may not be transferred same day. Update will follow from the Status Originator.
*`G003`-In a FIToFI Customer Credit Transfer: Credit to creditor’s account is pending receipt of required documents. The Status Originator has requested creditor to provide additional documentation. Update will follow from the Status Originator. 
In a Financial Institution Credit Transfer with cover: Status Originator has requested a previous Agent to provide additional information/correct information. Update will follow from the Status Originator.
*`G004`-In a FIToFI Customer Credit Transfer: Credit to the creditor’s account is pending, status Originator is waiting for funds provided via a cover. Update will follow from the Status Originator.
*`G005`-Payment has been delivered to creditor agent with service level.
*`G006`-Payment has been delivered to creditor agent without service level.
*`ID01`-Signature file was sent to the bank but the corresponding original file has not been sent yet.
*`MD01`-No Mandate
*`MD02`-Mandate related information data required by the scheme is missing.
*`MD05`-Creditor or creditor's agent should not have collected the direct debit
*`MD06`-Return of funds requested by end customer
*`MD07`-End customer is deceased.
*`MS02`-Reason has not been specified by end customer
*`MS03`-Reason has not been specified by agent.
*`NARR`-Reason is provided as narrative information in the additional reason information.
*`NERI`-Credit transfer is tagged as an Extended Remittance Information (ERI) transaction but does not contain ERI.
*`RC01`-Bank identifier code specified in the message has an incorrect format (formerly IncorrectFormatForRoutingCode).
*`RC02`-Bank identifier is invalid or missing.
Generic usage if cannot specify between debit or credit account
*`RC03`-Debtor bank identifier is invalid or missing
*`RC04`-Creditor bank identifier is invalid or missing
*`RC05`-BIC identifier is invalid or missing.
Generic usage if cannot specify between debit or credit account.
*`RC06`-Debtor BIC identifier is invalid or missing
*`RC07`-Creditor BIC identifier is invalid or missing
*`RC08`-ClearingSystemMemberidentifier is invalid or missing.
Generic usage if cannot specify between debit or credit account
*`RC09`-Debtor ClearingSystemMember identifier is invalid or missing
*`RC10`-Creditor ClearingSystemMember identifier is invalid or missing
*`RC11`-Intermediary Agent is invalid or missing
*`RC12`-Creditor Scheme Id is invalid or  missing
*`RCON`-Conflict with R-Message
*`RECI`-Further information regarding the intended recipient.
*`RF01`-Transaction reference is not unique within the message.
*`RR01`-Specification of the debtor’s account or unique identification needed for reasons of regulatory requirements is insufficient or missing
*`RR02`-Specification of the debtor’s name and/or address needed for regulatory requirements is insufficient or missing.
*`RR03`-Specification of the creditor’s name and/or address needed for regulatory requirements is insufficient or missing.
*`RR04`-Regulatory Reason
*`RR05`-Regulatory or Central Bank Reporting information missing, incomplete or invalid.
*`RR06`-Tax information missing, incomplete or invalid.
*`RR07`-Remittance information structure does not comply with rules for payment type.
*`RR08`-Remittance information truncated to comply with rules for payment type.
*`RR09`-Structured creditor reference invalid or missing.
*`RR10`-Character set supplied not valid for the country and payment type.
*`RR11`-Invalid or missing identification of a bank proprietary service.
*`RR12`-Invalid or missing identification required within a particular country or payment type.
*`S000`-Request for Cancellation is acknowledged following validation.
*`S001`-Unique End-to-end Transaction Reference (UETR) relating to a payment has been identified as being associated with a Request for Cancellation.
*`S002`-Unique End-to-end Transaction Reference (UETR) relating to a payment has been prevent from traveling across a messaging network.
*`S003`-Request for Cancellation has been forwarded to the payment processing/last payment processing agent.
*`S004`-Request for Cancellation has been acknowledged as delivered to payment processing/last payment processing agent.
*`SL01`-Due to specific service offered by the Debtor Agent.
*`SL02`-Due to specific service offered by the Creditor Agent.
*`SL03`-Due to a specific service offered by the clearing system.
*`SL11`-Whitelisting service offered by the Debtor Agent; Debtor has not included the Creditor on its “Whitelist” (yet). In the Whitelist the Debtor may list all allowed Creditors to debit Debtor bank account.
*`SL12`-Blacklisting service offered by the Debtor Agent; Debtor included the Creditor on his “Blacklist”. In the Blacklist the Debtor may list all Creditors not allowed to debit Debtor bank account.
*`SL13`-Due to Maximum allowed Direct Debit Transactions per period service offered by the Debtor Agent.
*`SL14`-Due to Maximum allowed Direct Debit Transaction amount service offered by the Debtor Agent.
*`TA01`-The transmission of the file was not successful – it had to be aborted (for technical reasons)
*`TD01`-There is no data available (for download)
*`TD02`-The file cannot be read (e.g. unknown format)
*`TD03`-The file format is incomplete or invalid
*`TK01`-Token is invalid.
*`TK02`-Token used for the sender does not exist.
*`TK03`-Token used for the receiver does not exist.
*`TK09`-Token required for request is missing.
*`TKCM`-Token found with counterparty mismatch.
*`TKSG`-Single Use Token already used.
*`TKSP`-Token found with suspended status.
*`TKVE`-Token found with value limit rule violation.
*`TKXP`-Token expired.
*`TM01`-Associated message, payment information block, or transaction was received after agreed processing cut-off time.
*`TS01`-The (technical) transmission of the file was successful.
*`TS04`-The order was transferred to pass by accompanying note signed by hand
*`CN01`-Authorisation is cancelled.
*`FOCR`-Return following a cancellation request.
*`FR01`-Returned as a result of fraud.
*`NOAS`-No response from Beneficiary.
*`NOCM`-Customer account is not compliant with regulatory requirements, for example FICA (in South Africa) or any other regulatory requirements which render an account inactive for certain processing.
*`RUTA`-Return following investigation request and no remediation possible.
*`UPAY`-Payment is not justified.
*`AEXR`-Request-to-pay Expiry Date and Time has already passed.
*`ALAC`-Request-to-pay has already been accepted by the Debtor.
*`ARFR`-Request-to-pay has already been refused by the Debtor.
*`ARJR`-Request-to-pay has already been rejected.
*`ATNS`-Attachments to the request-to-pay are not supported.
*`EDTL`-Expiry date time of the request-to-pay is too far in the future.
*`EDTR`-Expiry date time of the request-to-pay is already reached.
*`FRAD`-Cancellation requested following a transaction that was originated fraudulently. The use of the FraudulentOrigin code should be governed by jurisdictions.
*`IEDT`-Expiry date time of the request-to-pay is incorrect.
*`IRNR`-No initial request-to-pay has been received.
*`NOAR`-No existing agreement for receiving request-to-pay messages.
*`NOPG`-Requested payment guarantee (by Creditor) related to a request-to-pay cannot be provided.
*`NRCH`-Recipient side of the request-to-pay (payer or its request-to-pay service provider) is not reachable.
*`PINS`-Type of payment requested in the request-to-pay is not supported by the payer.
*`REPR`-Request-to-pay has been received and can be processed further.
*`RTNS`-Debtor does not support request-to-pay transactions.
*`SPII`-Identifier of the request-to-pay service provider is incorrect.
*`UCRD`-Unknown Creditor.
*`FF12`-Original payment is not eligible to be returned given its current status.
*`FF13`-No record of request for cancellation found.
*`DC02`-Rejection of a payment due to covering FI settlement not being received.
*`APAR`-Request To Pay has already been paid by the Debtor.
*`AB26`-Settlement Instruction does not exist.
*`AB12`-Duplicate Concurrent Batch Sequence number– for Settlement Instructions.
*`AB13`-Wrong Message Routing Type for Return-of-Funds.
*`AB15`-Instruction may not be placed on the Continuous Processing Line settlement processor.
*`AB21`-Agreement number not valid (beneficiary).
*`BDAY`-Settlement Cycle Day and Calendar day should be the same.
*`DS28`-Message routed to the wrong environment.
*`INDT`-Details not valid for this field.
*`ISWS`-Cannot schedule instruction for Night Window.
*`MINF`-Information missing for the field or cannot be empty.
*`NOFR`-Continuous Processing Line on Hold Instruction.
*`RC13`-Originator not active any more.
*`RC15`-Settlement agreement required.
*`RC16`-Participant blocked from SADC-RTGS.
*`SBRN`-Remove Concurrent Batch Processing Line on hold instruction.
*`RQNR`-Payer did not recognize the request from Payee Participant,
*`SNRD`-Services are not yet rendered by the Payee Participant (Creditor).
*`OSNS`-Requested optional service (for example instalment payments) is not supported.
*`AMSE`-Size of the attachment exceeds the allowed maximum.
*`INAR`-Payer’s activation reference is invalid.
*`EDNA`-Requested execution date of the payment is not accepted.
*`SL15`-Maximum number of credit transactions allowed by the account servicer per service period exceeded.
*`SL16`-Maximum total credit amount allowed by the account servicer per service period exceeded.
*`SL17`-Whitelisting service offered by payment system operator or financial institution. Debtor is not included on the Creditor side whitelist.
*`SL18`-Blacklisting service offered by payment system operator or financial institution. Debtor included on the Creditor side blacklist.
*`CHRG`-Related to a Charge message to convey that the charge bearer code used in the corresponding Payment message was not debt.
*`CHCO`-Related to a Charge message to convey that the code in Charge Breakdown / Type / Code is not accepted by the receiving party.
*`IPNS`-Payments in instalments are not supported.
*`CNNS`-Credit notes are not supported.
*`EOL1`-Expiration of the payment authorisation due to no use for too long.
*`PNRT`-Error code used for RTP-initiated CTR when the pacs.008 details are not aligned with the pain.013 request.
*`OBO1`-Settlement of the transaction has been completed and is reported by an intermediary agent or Payment Market Infrastructure on behalf of the Creditor Agent. The credited amount is known.
*`OBO2`-Settlement of the transaction has been completed and is reported by an intermediary agent or Payment Market Infrastructure on behalf of the Creditor Agent. The credited amount is not known.
*`G007`-The payment has been passed by the Payment Market Infrastructure to the next agent in the payment chain; receipt has not yet been confirmed.
*`G008`-The payment has been received by the next agent via the Payment Market Infrastructure.
*`IMCC`-Invalid Merchant Category Code
*`IUCT`-Invalid Use Case Type
*`INCT`-Invalid Channel Type
*`AEML`-Requested amount exceeds the limit set by Debtor (Agent)
*`WGDA`-Wrong Debtor Agent in charge request message
*`WGDB`-Wrong Debtor in charge request message
*`UTNV`-Referenced transaction not found
*`MICT`-Multiple identical Charge Types in Charge Breakdown
*`GUAG`-Guaranteed Agreement with Correspondent, therefore Correspondent is the liable party

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 4
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | AB01 |
| 2 | AB02 |
| 3 | AB03 |
| 4 | AB04 |
| 5 | AB05 |
| 6 | AB06 |
| 7 | AB07 |
| 8 | AB08 |
| 9 | AB09 |
| 10 | AB10 |
| 11 | AB11 |
| 12 | AC01 |
| 13 | AC02 |
| 14 | AC03 |
| 15 | AC04 |
| 16 | AC05 |
| 17 | AC06 |
| 18 | AC07 |
| 19 | AC08 |
| 20 | AC09 |
| 21 | AC10 |
| 22 | AC11 |
| 23 | AC12 |
| 24 | AC13 |
| 25 | AC14 |
| 26 | AC15 |
| 27 | AC16 |
| 28 | AG01 |
| 29 | AG02 |
| 30 | AG03 |
| 31 | AG04 |
| 32 | AG05 |
| 33 | AG06 |
| 34 | AG07 |
| 35 | AG08 |
| 36 | AG09 |
| 37 | AG10 |
| 38 | AG11 |
| 39 | AG12 |
| 40 | AG13 |
| 41 | AGNT |
| 42 | AM01 |
| 43 | AM02 |
| 44 | AM03 |
| 45 | AM04 |
| 46 | AM05 |
| 47 | AM06 |
| 48 | AM07 |
| 49 | AM09 |
| 50 | AM10 |
| 51 | AM11 |
| 52 | AM12 |
| 53 | AM13 |
| 54 | AM14 |
| 55 | AM15 |
| 56 | AM16 |
| 57 | AM17 |
| 58 | AM18 |
| 59 | AM19 |
| 60 | AM20 |
| 61 | AM21 |
| 62 | AM22 |
| 63 | AM23 |
| 64 | BE01 |
| 65 | BE04 |
| 66 | BE05 |
| 67 | BE06 |
| 68 | BE07 |
| 69 | BE08 |
| 70 | BE09 |
| 71 | BE10 |
| 72 | BE11 |
| 73 | BE12 |
| 74 | BE13 |
| 75 | BE14 |
| 76 | BE15 |
| 77 | BE16 |
| 78 | BE17 |
| 79 | BE18 |
| 80 | BE19 |
| 81 | BE20 |
| 82 | BE21 |
| 83 | BE22 |
| 84 | BE23 |
| 85 | CERI |
| 86 | CH03 |
| 87 | CH04 |
| 88 | CH07 |
| 89 | CH09 |
| 90 | CH10 |
| 91 | CH11 |
| 92 | CH12 |
| 93 | CH13 |
| 94 | CH14 |
| 95 | CH15 |
| 96 | CH16 |
| 97 | CH17 |
| 98 | CH19 |
| 99 | CH20 |
| 100 | CH21 |
| 101 | CH22 |
| 102 | CHQC |
| 103 | CNOR |
| 104 | CURR |
| 105 | CUST |
| 106 | DNOR |
| 107 | DS01 |
| 108 | DS02 |
| 109 | DS03 |
| 110 | DS04 |
| 111 | DS05 |
| 112 | DS06 |
| 113 | DS07 |
| 114 | DS08 |
| 115 | DS09 |
| 116 | DS0A |
| 117 | DS0B |
| 118 | DS0C |
| 119 | DS0D |
| 120 | DS0E |
| 121 | DS0F |
| 122 | DS0G |
| 123 | DS0H |
| 124 | DS0K |
| 125 | DS10 |
| 126 | DS11 |
| 127 | DS12 |
| 128 | DS13 |
| 129 | DS14 |
| 130 | DS15 |
| 131 | DS16 |
| 132 | DS17 |
| 133 | DS18 |
| 134 | DS19 |
| 135 | DS20 |
| 136 | DS21 |
| 137 | DS22 |
| 138 | DS23 |
| 139 | DS24 |
| 140 | DS25 |
| 141 | DS26 |
| 142 | DS27 |
| 143 | DT01 |
| 144 | DT02 |
| 145 | DT03 |
| 146 | DT04 |
| 147 | DT05 |
| 148 | DT06 |
| 149 | DU01 |
| 150 | DU02 |
| 151 | DU03 |
| 152 | DU04 |
| 153 | DU05 |
| 154 | DUPL |
| 155 | ED01 |
| 156 | ED03 |
| 157 | ED05 |
| 158 | ED06 |
| 159 | ERIN |
| 160 | FF01 |
| 161 | FF02 |
| 162 | FF03 |
| 163 | FF04 |
| 164 | FF05 |
| 165 | FF06 |
| 166 | FF07 |
| 167 | FF08 |
| 168 | FF09 |
| 169 | FF10 |
| 170 | FF11 |
| 171 | G000 |
| 172 | G001 |
| 173 | G002 |
| 174 | G003 |
| 175 | G004 |
| 176 | G005 |
| 177 | G006 |
| 178 | ID01 |
| 179 | MD01 |
| 180 | MD02 |
| 181 | MD05 |
| 182 | MD06 |
| 183 | MD07 |
| 184 | MS02 |
| 185 | MS03 |
| 186 | NARR |
| 187 | NERI |
| 188 | RC01 |
| 189 | RC02 |
| 190 | RC03 |
| 191 | RC04 |
| 192 | RC05 |
| 193 | RC06 |
| 194 | RC07 |
| 195 | RC08 |
| 196 | RC09 |
| 197 | RC10 |
| 198 | RC11 |
| 199 | RC12 |
| 200 | RCON |
| 201 | RECI |
| 202 | RF01 |
| 203 | RR01 |
| 204 | RR02 |
| 205 | RR03 |
| 206 | RR04 |
| 207 | RR05 |
| 208 | RR06 |
| 209 | RR07 |
| 210 | RR08 |
| 211 | RR09 |
| 212 | RR10 |
| 213 | RR11 |
| 214 | RR12 |
| 215 | S000 |
| 216 | S001 |
| 217 | S002 |
| 218 | S003 |
| 219 | S004 |
| 220 | SL01 |
| 221 | SL02 |
| 222 | SL03 |
| 223 | SL11 |
| 224 | SL12 |
| 225 | SL13 |
| 226 | SL14 |
| 227 | TA01 |
| 228 | TD01 |
| 229 | TD02 |
| 230 | TD03 |
| 231 | TK01 |
| 232 | TK02 |
| 233 | TK03 |
| 234 | TK09 |
| 235 | TKCM |
| 236 | TKSG |
| 237 | TKSP |
| 238 | TKVE |
| 239 | TKXP |
| 240 | TM01 |
| 241 | TS01 |
| 242 | TS04 |
| 243 | CN01 |
| 244 | FOCR |
| 245 | FR01 |
| 246 | NOAS |
| 247 | NOCM |
| 248 | RUTA |
| 249 | UPAY |
| 250 | AEXR |
| 251 | ALAC |
| 252 | ARFR |
| 253 | ARJR |
| 254 | ATNS |
| 255 | EDTL |
| 256 | EDTR |
| 257 | FRAD |
| 258 | IEDT |
| 259 | IRNR |
| 260 | NOAR |
| 261 | NOPG |
| 262 | NRCH |
| 263 | PINS |
| 264 | REPR |
| 265 | RTNS |
| 266 | SPII |
| 267 | UCRD |
| 268 | FF12 |
| 269 | FF13 |
| 270 | DC02 |
| 271 | APAR |
| 272 | AB26 |
| 273 | AB12 |
| 274 | AB13 |
| 275 | AB15 |
| 276 | AB21 |
| 277 | BDAY |
| 278 | DS28 |
| 279 | INDT |
| 280 | ISWS |
| 281 | MINF |
| 282 | NOFR |
| 283 | RC13 |
| 284 | RC15 |
| 285 | RC16 |
| 286 | SBRN |
| 287 | RQNR |
| 288 | SNRD |
| 289 | OSNS |
| 290 | AMSE |
| 291 | INAR |
| 292 | EDNA |
| 293 | SL15 |
| 294 | SL16 |
| 295 | SL17 |
| 296 | SL18 |
| 297 | CHRG |
| 298 | CHCO |
| 299 | IPNS |
| 300 | CNNS |
| 301 | EOL1 |
| 302 | PNRT |
| 303 | OBO1 |
| 304 | OBO2 |
| 305 | G007 |
| 306 | G008 |
| 307 | IMCC |
| 308 | IUCT |
| 309 | INCT |
| 310 | AEML |
| 311 | WGDA |
| 312 | WGDB |
| 313 | UTNV |
| 314 | MICT |
| 315 | GUAG |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
