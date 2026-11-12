---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementTransactionModificationRequestStatusAdvice sese.039.001.08"]
content_origin: "source-transcription"
---

# SecuritiesSettlementTransactionModificationRequestStatusAdvice sese.039.001.08

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Business Examples / SecuritiesSettlementTransactionModificationRequestStatusAdvice sese.039.001.08.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3187** SecuritiesSettlementTransactionModificationRequestStatusAdvice sese.039.001.08

**P3188** Description

**P3189** On the 14 January 2019, Dresdner Bank London (DRESGB2L) informs Dresdner Bank Frankfurt (DRESDEFF) the account owner, on the status of a previously sent modification instruction. This is done through a Securities settlement Transaction Modification Request Status Advice (sese.039.001.04).

**P3190** Business Data

**P3191** Account Owner: DRESDEFF

**P3192** Account Owner Transaction Identification: FRTJ123DEL

**P3193** Modification Request Reference: sese.038.001.04

**P3194** Safekeeping Account: 222S

**P3195** Modification Processing Status: Acknowledged/Accepted (no reason)

**P3196** Message Instance

**P3197** <SctiesSttlmTxModReqStsAdvc>

**P3198**      <ModReqRef>

**P3199**           <Id>sese.038.001.04</Id>

**P3200**      </ModReqRef>

**P3201**      <AcctOwnr>

**P3202**           <AnyBIC>DRESDEFF</AnyBIC>

**P3203**      </AcctOwnr>

**P3204**      <SfkpgAcct>

**P3205**           <Id>222S</Id>

**P3206**      </SfkpgAcct>

**P3207**      <TxId>

**P3208**           <AcctOwnrTxId>FRTJ123DEL</AcctOwnrTxId>

**P3209**      </TxId>

**P3210**      <ModPrcgSts>

**P3211**           <AckdAccptd>

**P3212**                <NoSpcfdRsn>NORE</NoSpcfdRsn>

**P3213**           </AckdAccptd>

**P3214**      </ModPrcgSts>

**P3215** </SctiesSttlmTxModReqStsAdvc>	

