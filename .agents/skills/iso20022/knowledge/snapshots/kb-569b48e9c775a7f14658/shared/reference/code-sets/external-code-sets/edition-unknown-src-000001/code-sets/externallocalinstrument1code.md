---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalLocalInstrument1Code"]
code_set: "ExternalLocalInstrument1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalLocalInstrument1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalLocalInstrument1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external local instrument code in the format of character string with a maximum length of 35 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`DDMC`-Transaction is related to a direct debit instruction authorized under a confirmed electronic mandate.
*`DDMP`-Transaction is related to a direct debit instruction authorized under a paper based mandate, supported by paper authorization signed by the debtor.
*`DDMU`-Transaction is related to a direct debit instruction authorized under an unconfirmed electronic mandate requiring confirmation by the debtor.
*`BPA`-Transaction is related to an Instant Credit Transfer under the rules of the Centrale Bank van Aruba, based on the EPC SCT Inst scheme, with a specific batch time-out delay.
*`IPA`-Transaction is related to an Instant Credit Transfer under the rules of the Centrale Bank van Aruba, based on the EPC SCT Inst scheme.
*`TRF`-Transaction is related to credit transfers
*`82`-Transaction is related to a direct debit that is not pre authorised (Einzugsermächtigung).
*`83`-Transaction is related to a direct debit that is pre authorised (Abbuchungsauftrag).
*`CPP`-Transaction is related to cash per post.
Transaction to ultimate recipient having no bank account. Primary beneficiary is a postal service provider. Funds are paid out by cash. Additional necessary information for address and delivery options need to be attached.

*`RTR`-Transaction is related to returned credit transfers.
*`GST`-Transaction is related to truncated credit transfers.
Conversion of physical instrument to electonric form for transmission to the paying bank and where the original paper document does not continue in the clearing process..The original instrument rules are retained throughout the life of the instrument.
Transaction triggered by specific marked and populated paper slip.
Reconciliation reference is secured by check digits supporting secure optical recognition. All other remittance information is truncated prior transmission.

*`DDT`-Transaction is related to direct debits.
*`RDD`-Transaction is related to returned direct debits.
*`CHN`-Transaction is related to truncated checks.
Conversion of physical instrument to electonric form for transmission to the paying bank and where the original paper document does not continue in the clearing process..The original instrument rules are retained throughout the life of the instrument.
*`STR`-Transaction is related to revoked credit transfers
*`SDD`-Transaction is related to revoked direct debits.
*`SRT`-Transaction is related to revoked returned credit transfers
*`SRD`-Transaction is related to revoked returned direct debits.
*`SCN`-Transaction is related to revoked truncated checks.
*`SGT`-Transaction is related to revoked truncated credit transfers.
*`CARD`-Transaction is related to card clearing.
*`05`-Transaction is related to a direct debit that is not pre authorised (Einzugsermächtigung).
*`04`-Transaction is related to a direct debit that is pre authorised (Abbuchungsauftrag).
*`ISE`-Transaction is related to the German Image-based Cheque Collection Procedure “Imagegestützter Scheckeinzug - ISE”
*`BSE`-Transaction is related to the German Paperless Cheque Collection procedure “Belegloser Scheckeinzug - BSE”
*`58`-Transaction is related to a business-to-business direct debit (CSB58).
*`19`-Transaction is related to a business-to-customer direct debit (CSB19).
*`ASTI`-Indicates that the payment is sent by an authorized third party on behalf of the participant.
*`BACP`-Indicates that the payment was initiated manually using a GUI (Graphical User Interface).
*`MANP`-Indicates that the payment is sent by responsible Central Bank on behalf of the participant in case of contingency.
*`SBTI`-Indicates that the payment is submitted to move  liquidity to the technical account - dedicated to real-time settlement in an external system (for example ancillary system) . The payment is processed in a separate payment queue besides the normal processing.
*`85`-Transaction is related to an urgent direct debit that is pre authorised (Avis de Prélèvement accéléré).
*`08`-Transaction is related to a direct debit that is pre authorised (Avis de Prélèvement).
*`89`-Transaction is related to an urgent direct debit that is pre authorised (Avis de Prélèvement vérifié).
*`60`-LCR - Lettre de Change Relevé (Recovered Bill of Exchange) and BOR - Billet à Orde Relevé (Promissory Note)
*`RIBA`-Transaction is related to a non-pre authorised collection (RIBA).
*`RIDO`-Transaction is related to a direct debit that is pre authorised and revocable (RID Ordinario).
*`RIDV`-Transaction is related to an urgent direct debit that is pre authorised and revocable (RID Veloce).
*`IDEAL`-Transaction is related to payments via internet owned by Currence.
*`INSTNT01`-The transaction is related to a regular  Credit Transfer and will be instantly processed under the Dutch AOS on top of the EPC SCT scheme.
*`INSTTC01`-The transaction is related to an Instant Credit Transfer under the rules of the Dutch AOS on top of the EPC SCT Inst scheme.
*`INSTIDEAL`-Transaction is related to payments via internet owned by Currence which uses an Instant Credit Transfer.
*`INSTNT01IDEAL`-Transaction is related to payments via internet owned by Currence which uses a regular  Credit Transfer and will be instantly processed under the Dutch AOS on top of the EPC SCT scheme.
*`INSTTC01IDEAL`-Transaction is related to payments via internet owned by Currence which uses an Instant Credit Transfer under the rules of the Dutch AOS on top of the EPC SCT Inst scheme.
*`NLDO`-Transaction is related to a Domestic payment initiated by PAIN.001
*`NLUP`-Transaction is related to a Domestic payment initiated by PAIN.001
*`SDN`-Transaction is related to payments via a ‘Standaard Digitale Nota’ InvoiceAcceptgiro payment.
*`ACCEPT`-Transaction is related to payments via Acceptgiro owned by Currence.
*`ICMC`-Transaction is related to an Incident Management Correction procedure based on the DD infrastructure.
*`NLGOV`-Transaction is related to direct debit scheme owned by the NVB.
*`IN`-Transaction is related to cross border customer credit transfer.
*`ONCL`-Transaction is related to overnight clearing.
*`PERI`-Credit transfer contains Extended Remittance Information (ERI) as defined within the applicable scheme.
*`SDCL`-Transaction is related to New Zealand High Value Clearing System (HVCS) same day clearing payments.
*`DDNR`-SEPA Core Direct Debit with ‘no refund’ option
*`DDFA`-SEPA Fixed Amount Direct Debit
*`CORE`-Transaction is related to SEPA direct debit -core.
*`B2BAMIPM`-SEPA B2B Direct Debit AMI based on a paper mandate
*`B2B`-Transaction is related to SEPA business to business direct debit.
*`CR1AMIPM`-Optional shorter time cycle (D-1) for SEPA Core Direct Debit AMI based on a paper mandate
*`CORAMIPM`-SEPA Core Direct Debit AMI based on a paper mandate
*`COR1`-Optional shorter time cycle (D-1) for SEPA Core Direct Debit
*`FADAMIPM`-SEPA Fixed Amount Direct Debit AMI based on a paper mandate
*`CLSCCPERX`-Transaction is related to the CLSClearedFX service for Eurex.  
Usage: The code is mandatory for all pacs.009 payments to this service.
*`CLSCCPLCH`-Transaction is related to the CLSClearedFX service for London Exchange Clearing House. 
Usage: The code is mandatory for all pacs.009 payments to this service.
*`INST`-Transaction is related to an Instant Credit Transfer.
Use case example: SEPA Instant Credit Transfer (SCT Inst)
*`ADD`-Transaction is authenticated direct debit for domestic use.
*`UDD`-Transaction is unauthenticated direct debit for domestic use.
*`CCI`-Transaction is related to an intra-group bank initiated cash management payment
*`IAT`-Transaction is related to international ACH.
*`CCD`-Transaction is related to cash concentration or disbursement corporate counterparty.
*`CTX`-Transaction is related to corporate trade exchange.
*`PPD`-Transaction is related to prearranged payment or deposit consumer counterparty.
*`CIE`-A credit entry initiated by or on behalf of the holder of a consumer account
*`RCK`-Transaction is related to re-presented check entry.
*`ARC`-Transaction is related to accounts receivable check.
*`WEB`-Transaction is related to internet initiated entry.
*`POP`-Transaction is related to point-of-purchase.
*`POS`-Transaction is related to point-of-sale.
*`TEL`-Transaction is related to telephone initiated entry.
*`ITP`-Payment via Instant Credit Transfer but Credit Transfer is also possible.
*`CTP`-Payment via Credit Transfer but Instant Credit Transfer is also possible.
*`MDP`-Type of New Payments Architecture (NPA) payment. Payments are processed over a three-day cycle and available to customers early in the morning of Day 3.
*`IMD`-Type of Payment used within the New Payments Architecture (UK). Immediate Payments are used for payments initiated by customers using channels such as internet, mobile or telephone banking, where the customer wants the payment to be effected immediately.
*`SOP`-Standing Orders are regular payments of a fixed amount paid to the same recipient on a specified date, for example, to pay rent.
*`FDP`-Type of Payment used within the New Payments Architecture (UK). Forward-dated payments are one-off payments sent and received on a pre-arranged date, set-up by the customer in advance, for example, to pay a bill.
*`NACH`-Payment via the Indian NACH clearing (net settlement).
*`NEFT`-Payment via the Indian NEFT clearing (net settlement).
*`IMPS`-Instant payment via the Indian IMPS clearing system.
*`IUPI`-Instant payment via the Indian UPI clearing system.

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 35
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | DDMC |
| 2 | DDMP |
| 3 | DDMU |
| 4 | BPA |
| 5 | IPA |
| 6 | TRF |
| 7 | 82 |
| 8 | 83 |
| 9 | CPP |
| 10 | RTR |
| 11 | GST |
| 12 | DDT |
| 13 | RDD |
| 14 | CHN |
| 15 | STR |
| 16 | SDD |
| 17 | SRT |
| 18 | SRD |
| 19 | SCN |
| 20 | SGT |
| 21 | CARD |
| 22 | 05 |
| 23 | 04 |
| 24 | ISE |
| 25 | BSE |
| 26 | 58 |
| 27 | 19 |
| 28 | ASTI |
| 29 | BACP |
| 30 | MANP |
| 31 | SBTI |
| 32 | 85 |
| 33 | 08 |
| 34 | 89 |
| 35 | 60 |
| 36 | RIBA |
| 37 | RIDO |
| 38 | RIDV |
| 39 | IDEAL |
| 40 | INSTNT01 |
| 41 | INSTTC01 |
| 42 | INSTIDEAL |
| 43 | INSTNT01IDEAL |
| 44 | INSTTC01IDEAL |
| 45 | NLDO |
| 46 | NLUP |
| 47 | SDN |
| 48 | ACCEPT |
| 49 | ICMC |
| 50 | NLGOV |
| 51 | IN |
| 52 | ONCL |
| 53 | PERI |
| 54 | SDCL |
| 55 | DDNR |
| 56 | DDFA |
| 57 | CORE |
| 58 | B2BAMIPM |
| 59 | B2B |
| 60 | CR1AMIPM |
| 61 | CORAMIPM |
| 62 | COR1 |
| 63 | FADAMIPM |
| 64 | CLSCCPERX |
| 65 | CLSCCPLCH |
| 66 | INST |
| 67 | ADD |
| 68 | UDD |
| 69 | CCI |
| 70 | IAT |
| 71 | CCD |
| 72 | CTX |
| 73 | PPD |
| 74 | CIE |
| 75 | RCK |
| 76 | ARC |
| 77 | WEB |
| 78 | POP |
| 79 | POS |
| 80 | TEL |
| 81 | ITP |
| 82 | CTP |
| 83 | MDP |
| 84 | IMD |
| 85 | SOP |
| 86 | FDP |
| 87 | NACH |
| 88 | NEFT |
| 89 | IMPS |
| 90 | IUPI |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
