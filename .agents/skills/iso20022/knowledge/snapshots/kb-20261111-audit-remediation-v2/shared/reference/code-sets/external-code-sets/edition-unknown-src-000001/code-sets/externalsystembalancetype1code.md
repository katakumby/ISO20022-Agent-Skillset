---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalSystemBalanceType1Code"]
code_set: "ExternalSystemBalanceType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalSystemBalanceType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalSystemBalanceType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the system balance type, as published in an external system balance type code set.
External code sets can be downloaded from www.iso20022.org.
*`ADJT`-Average balance to be held in the settlement account at the end of each day in order to fulfil the reserve due.
The approximation will be always made rounding up.
*`ADWR`-Balance represents the available discounted market value for discount window repo.
*`AIDR`-Balance represents the available discounted market value for intraday repo.
*`AVLB`-Balance of money or securities that is at the disposal of the account owner on the date specified.
*`BLCK`-Balance representing the regulatory reserve that a financial institution must have with the account servicing institution, such as the minimum credit balance a financial institution is to keep with its Central Bank for mandatory reserve purposes. In some countries, a blocked balance is known as a 'reserve' balance.
*`BLOC`-Balance representing the projected total of all cash legs for trades settling via a central securities depository that have been matched but blocked in order to not settle. These blocked trades are included in the calculation for settlement (for example to avoid overdrafts).
Usage rule: Blocking can be done by account owner or its counterparties. Usually this is done to chain transactions or to prioritise other trades. Blocked trades have an indicator that prevents the transactions from settling. Once matched, they can settle whenever the freeze is lifted. In this case they will move to FSET. Lifting the freeze can happen anytime during the day and the transaction will be settling in the next settlement cycle which can be the same day if the (international) central securities depository's operates several settlements cycles per day.
*`BOOK`-Balance that is registered in the books of the account servicer.
*`BSCC`-Balance represents the total of the bulk settlement and central moneymarkets unit processor credit.
*`BSCD`-Balance represents the total of the bulk settlement and central moneymarkets unit processor debit.
*`CCPS`-Balance representing the forecast of the total of all cash legs of transactions traded in exchanges that operate a central counterparty functionality.
*`CLSG`-Balance of the account at the end of the account servicer's business day. It is the sum of the opening balance at the beginning of the day and all entries booked to the account during the account servicer's business day.
*`COHB`-Balance representing the total incoming payments that were put on hold because the credit limit has been exceeded.
*`COLC`-Balance representing the projected total amount of all payment obligations to the participant (bank), based on their role as main paying agent.
*`CPBL`-Balance representing the total incoming payments that have been processed and are waiting for settlement.
*`CRDT`-Balance representing the sum of all credit entries booked to an account.
*`CRRT`-Balance of the account at a precise moment in time.
*`CUSA`-Balance representing the actual total of all asset servicing transactions such as dividends, income corporate actions equivalents, tax returns, redemptions, etc.
*`CUST`-Balance representing the projected total of all asset servicing transactions such as dividends, income corporate actions equivalents, tax returns, etc.
*`DBIT`-Balance representing the sum of all debit entries booked to an account.
*`DLOD`-Balance representing the intra day overdraft granted by the central bank to financial institutions participating in a RTGS system. This balance may vary over time and shall be offset at the end of the day.
*`DOHB`-Balance representing the total outgoing payments that were put on hold because the debit limit has been exceeded.
*`DPBL`-Balance representing the total outgoing payments that have been processed and are waiting for settlement.
*`DSET`-Balance representing the cash equivalent of all settled securities transactions.
*`DWRD`-Balance represents the discount window repo drawings.
*`EAST`-Balance representing the potential loan a Central Bank would make in cash if the collateral is pledged, such as securities available and eligible as collateral with the central bank.
*`EXRE`-The code defines the threshold to the value excess reserve exemption balance between the exempt and non-exempt tiers of excess reserve.
*`EXRR`-The code defines the balance beyond excess reserve exemption threshold within the periodic average balance for minimum reserve. Thus, this part of the excess reserve is still to be remunerated.
*`FCOL`-Balance representing the forecast of the cash-equivalent resulting from evaluation of existing holdings at central securities depositary that are qualified to serve as collateral.
*`FCOU`-Balance representing the cash equivalent resulting from evaluation of existing holdings at CSD that are qualified to serve as collateral and have been used as collateral.
*`FORC`-Balance representing the total of all balance types representing transactions to settle, blocked items and custody transactions.
*`FSET`-Balance representing the forecast of total of all cash legs for trades that are ready to settle via a central securities depository. Amounts shown are still subject to processing of the securities settlement.
*`FUND`-Balance representing the net amount to be funded resulting from all transactions which have an impact on the funding requirement.
*`FUTB`-Balance representing the total of the payments with a processing date in the future.
*`INTM`-Balance calculated in the course of the account servicer's business day, at the time specified, and subject to further changes during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified.
*`IRDR`-Balance represents the intraday repo drawings.
*`IRLT`-Balance represents the intraday repo limit.
*`LACK`-Balance representing the cash equivalent of transactions with a lack of holdings.
*`LRLD`-Balance of a specific limit value, such as a bilateral balance is calculated in relation to a given bilateral limit.
*`LTSF`-Balance composed of the sum of all liquidity transfers made to or from an account.
*`MSTR`-Balance of the identified account plus the balance of all of its subaccounts.
*`NOTE`-Balance representing the amount that a financial institution has set aside for a specific reason and which is therefore not available.
*`NSET`-Balance representing the cash equivalent of all non-settled securities transactions.
*`OPNG`-Book balance of the account at the beginning of the account servicer's business day. It always equals the closing book balance from the previous business day. 
Note: the available balance at the beginning of the account servicer's business day may be different from the closing book balance from the previous business day.
*`OTCC`-Balance representing the Forecast of the total of all cash-legs of transactions 'over the counter' (OTC), going through central counter party (CCP) functions.
*`OTCG`-Balance representing the forecast of the total of all cash legs of transactions traded 'over the counter' (OTC).
*`OTCN`-Balance representing the forecast of the total of all cash legs of transactions traded 'over the counter' (OTC) not going through central counter party (CCP) functions.
*`OTHB`-Balance representing the projected total of all cash legs for trades settling via a central securities depository that have been matched but blocked in order to not settle. These blocked transactions are not included in the calculation for settlement.
*`PDNG`-Balance of securities pending delivery, such as the orders to sell securities have been executed but settlement of the open transactions has not been confirmed.
*`PIPO`-Balance representing the fictive forecast of automated direct debits or payment based on standing arrangements between a central securities depository and the user.



Usage: Pay-Ins and Pay-Outs can be different based on individual payment instructions or available funds.
*`PRAV`-Average of the daily balances on the account used to fulfil the reserve requirements calculated from the beginning of the maintenance period.
*`PYMT`-Balance representing the sum of entries as a result of payments processing. Entries relating to fees, interest, or other movements not a result of payments sent or received by the account owner are not included.
*`REJB`-Balance representing the total of the payments that have been rejected.
*`REPC`-Balance represents the total of the central moneymarkets unit processor repo credits.
*`REPD`-Balance represents the total of the central moneymarkets unit processor repo debits.
*`REST`-Balance of cash that may only be used under certain conditions.

Balance type is used to block securities/cash in the client account for example, when related to specific corporate actions, the holding is under the direct control of the system paying agent, who is the only one who can transfer securities out of this balance type.
Also known as the "escrow balance" or "sequestered balance".
*`SAPC`-Balance represents the settlement account processor direct credit amount.
*`SAPD`-Balance represents the settlement account processor direct debit amount.
*`SAPP`-Balance represents the settlement account processor queue amount.
*`SCOL`-Balance representing the forecast of the cash-equivalent resulting from evaluation of the net incoming balance of securities qualified to serve as collateral for which settlement instructions are held at.
*`SCOU`-Balance representing the cash-equivalent resulting from evaluation of incoming securities, qualified to serve as collateral and actually used as collateral, which have been settled during the settlement process.
*`SELF`-Balance of the account identified (as opposed to Master Balance).
*`THRE`-Balance representing the amount that will be destined for investment. Difference between available balance and threshold for investment limit.
*`TOHB`-Balance representing the total of the payments that were put on hold because the limits have been exceeded.
*`TPBL`-Balance representing the total of the payments that have been processed and are waiting for settlement during the day.
*`XCHC`-Balance representing the forecast of the total of all cash legs of transactions in exchanges, going through CCP functions.
*`XCHG`-Balance representing the forecast of the total of all cash legs of transactions traded in exchanges.
*`XCHN`-Balance representing the forecast of the total of all cash legs of transactions traded in exchanges not going through central counter party (CCP) functions.
*`XCRD`-Balance, composed of booked entries and pending items known at the time of calculation, which projects the end of day credit balance if everything books to the account and no other credit entry is posted.
*`XDBT`-Balance, composed of booked entries and pending items known at the time of calculation, which projects the end of day debit balance if everything books to the account and no other debit entry is posted.
*`XPCD`-Balance, composed of booked entries and pending items known at the time of calculation, which projects the end of day balance if everything is booked on the account and no other entry is posted.

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
| 1 | ADJT |
| 2 | ADWR |
| 3 | AIDR |
| 4 | AVLB |
| 5 | BLCK |
| 6 | BLOC |
| 7 | BOOK |
| 8 | BSCC |
| 9 | BSCD |
| 10 | CCPS |
| 11 | CLSG |
| 12 | COHB |
| 13 | COLC |
| 14 | CPBL |
| 15 | CRDT |
| 16 | CRRT |
| 17 | CUSA |
| 18 | CUST |
| 19 | DBIT |
| 20 | DLOD |
| 21 | DOHB |
| 22 | DPBL |
| 23 | DSET |
| 24 | DWRD |
| 25 | EAST |
| 26 | EXRE |
| 27 | EXRR |
| 28 | FCOL |
| 29 | FCOU |
| 30 | FORC |
| 31 | FSET |
| 32 | FUND |
| 33 | FUTB |
| 34 | INTM |
| 35 | IRDR |
| 36 | IRLT |
| 37 | LACK |
| 38 | LRLD |
| 39 | LTSF |
| 40 | MSTR |
| 41 | NOTE |
| 42 | NSET |
| 43 | OPNG |
| 44 | OTCC |
| 45 | OTCG |
| 46 | OTCN |
| 47 | OTHB |
| 48 | PDNG |
| 49 | PIPO |
| 50 | PRAV |
| 51 | PYMT |
| 52 | REJB |
| 53 | REPC |
| 54 | REPD |
| 55 | REST |
| 56 | SAPC |
| 57 | SAPD |
| 58 | SAPP |
| 59 | SCOL |
| 60 | SCOU |
| 61 | SELF |
| 62 | THRE |
| 63 | TOHB |
| 64 | TPBL |
| 65 | XCHC |
| 66 | XCHG |
| 67 | XCHN |
| 68 | XCRD |
| 69 | XDBT |
| 70 | XPCD |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
